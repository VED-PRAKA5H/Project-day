import os
import html
from typing import List
from functools import wraps
from datetime import datetime
from send_mail import GmailSender
from flask_gravatar import Gravatar
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor.utils import cleanify
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CommentForm, LoginForm, PostForm, RegisterForm, CKEditor
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, delete, update, select, ForeignKey
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user

# Get current year for footer or other page info display
current_year = datetime.today().year

# -------------------- Flask App Configuration --------------------
app = Flask(__name__)
# Secret key for sessions and CSRF protection, loaded from environment variable
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

# Enable CKEditor extension for rich text editing in blog posts
ckeditor = CKEditor(app)

# Enable Bootstrap 5 styling integration
Bootstrap5(app)

# Setup Flask-Login manager for handling user login sessions
login_manager = LoginManager()
login_manager.init_app(app)

# Setup Flask-Gravatar for user avatar images by email
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# Function to load a user by ID for Flask-Login session management
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# -------------------- Database Setup --------------------
# Define base class for SQLAlchemy ORM models
class Base(DeclarativeBase):
    pass


# Database connection URI loaded from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

# Initialize SQLAlchemy instance with Base as model class
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Blog Post model with metadata and relationships
class Post(db.Model):
    __tablename__ = "post_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Unique ID for each post
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Title of blog post
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)  # Subtitle of blog post
    date: Mapped[str] = mapped_column(String(250), nullable=False)  # Date string for post
    body: Mapped[str] = mapped_column(Text, nullable=False)  # Full body content of the post
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # Author's name
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # URL for post image
    author_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))  # Foreign key reference to user
    user: Mapped["User"] = relationship(back_populates="posts")  # Relationship to User model
    comments: Mapped[List["Comment"]] = relationship()  # List of associated comments


# User model definition including authentication integration
class User(db.Model, UserMixin):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    posts: Mapped[List["Post"]] = relationship(back_populates='user')  # Posts authored by the user
    comments: Mapped[List["Comment"]] = relationship()  # Comments made by the user

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


# Comment model representing comments on blog posts
class Comment(db.Model):
    __tablename__ = "comment_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(250), nullable=False)  # Comment text
    commentator_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))  # ID of comment author
    commentator: Mapped["User"] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))  # ID of associated post
    post: Mapped["Post"] = relationship(back_populates="comments")


# Create all database tables (if not existing) when app context is ready
with app.app_context():
    db.create_all()


# -------------------- Helper Functions --------------------
# Retrieve all posts from the database
def get_blog_data():
    stmt = select(Post)
    blogs = db.session.execute(stmt).scalars().all()
    return blogs


# Initialize Gmail sender utility for contact form emails
gs = GmailSender()


# -------------------- Flask Routes --------------------

# Home page route - display all blog posts with user login state
@app.route("/")
def home():
    data = get_blog_data()
    if current_user.is_authenticated:
        id_ = current_user.id
    else:
        id_ = 2  # Default or guest ID
    return render_template(template_name_or_list='index.html',
                           year=current_year,
                           posts=data,
                           logged_in=current_user.is_authenticated,
                           user_id=id_
                           )


# User registration route handling GET and POST
@app.route('/register', methods=['POST', "GET"])
def register():
    registerform = RegisterForm()
    if request.method == "POST":
        # Check if user with entered email already exists
        stmt = select(User).where(User.email == request.form.get('email'))
        user = db.session.execute(stmt).scalar()
        if user is None:
            user_data = {"name": request.form.get('name'),
                         "email": request.form.get("email"),
                         "password": request.form.get('password')}
            # Hash the password before saving
            user_data['password'] = generate_password_hash(user_data['password'], method='pbkdf2:sha256', salt_length=8)
            new_user = User(**user_data)
            db.session.add(new_user)
            db.session.commit()
            # Log in the new user immediately
            login_user(new_user)
            return redirect(url_for('home'))
        else:
            flash('This email has been already registered. Login instead.')
            return redirect(url_for('login'))

    return render_template('register.html', form=registerform, logged_in=current_user.is_authenticated)


# User login route handling GET and POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        stmt = select(User).where(User.email == email)
        user = db.session.execute(stmt).scalar()
        if user is not None:
            # Check password hash for authentication
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Incorrect Password.')
                return render_template('login.html', form=loginform, logged_in=current_user.is_authenticated)
        else:
            flash(f'This email is not registered, please register first.')
            return redirect(url_for('register'))

    return render_template("login.html", form=loginform)


# Logout route requires login
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# Static about page route
@app.route("/about")
def about():
    return render_template('about.html', year=current_year, logged_in=False)


# Contact page to send emails on form submission
@app.route("/contact", methods=['GET', "POST"])
def contact():
    if request.method == 'POST':
        # Collect submitted form data
        form_data = {
            'Name': request.form.get('name'),
            'Email': request.form.get('email'),
            'Phone': request.form.get('phone'),
            'Message': request.form.get('message'),
        }
        # Format details for email body
        details = ""
        for key, value in form_data.items():
            details += f"{key}: {value}\n"

        # Send email using GmailSender class
        gs.send_mail(user_detail=details)
        return render_template('success.html', year=current_year, logged_in=False)

    else:
        return render_template('contact.html', year=current_year, logged_in=False)


# Single blog post page to show post and its comments, handle comment submission
@app.route("/post/<int:num>", methods=["POST", 'GET'])
def get_post(num):
    commentform = CommentForm()
    # Fetch requested post by id
    current_post = db.session.execute(select(Post).where(Post.id == num)).scalar()
    # Fetch comments for this post
    stmt = select(Comment).where(Comment.post_id == num)
    all_comments = db.session.execute(stmt).scalars().all()
    if request.method == "POST":
        if current_user.is_authenticated:
            comment = request.form.get('comment')
            new_comment = Comment(commentator=current_user, text=comment, post=current_post)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('get_post', num=num))
        else:
            flash("You need to login or register first.")
            return redirect(url_for('login'))
    else:
        if current_user.is_authenticated:
            id_ = current_user.id
        else:
            id_ = 2  # Guest or default id

        return render_template(template_name_or_list='post.html',
                               post=current_post,
                               comments=all_comments,
                               year=current_year,
                               logged_in=current_user.is_authenticated,
                               user_id=id_,
                               form=commentform,
                               gravatar=gravatar
                               )


# Decorator to restrict route access to admin user only (user id=1)
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id == 1:
            result = f(*args, **kwargs)
            return result
        else:
            abort(404)  # Return 404 error if not admin

    return decorated_function


# Route for creating a new blog post (admin only)
@app.route("/newpost", methods=['POST', 'GET'])
@admin_only
@login_required
def create_post():
    if request.method == "POST":
        # Extract post data from form and clean html content
        post_data = request.form.to_dict()
        post_data.pop('csrf_token')
        post_data.pop('submit_btn')
        post_data['body'] = cleanify(post_data['body'])
        post_data['body'] = html.unescape(post_data['body'])

        # Create new Post instance and add to DB
        new_post = Post(user=current_user, **post_data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        postform = PostForm()
        return render_template('new_post.html', form=postform, year=current_year,
                               logged_in=current_user.is_authenticated)


# Route to delete a blog post by ID (admin only)
@app.route("/delete/<num>", methods=['POST'])
@admin_only
@login_required
def delete_post(num):
    if request.method == 'POST':
        stmt = delete(Post).where(Post.id == int(num))
        db.session.execute(stmt)
        db.session.commit()
        db.session.close()

    return redirect(url_for('home'))


# Route to edit an existing blog post (admin only)
@app.route("/edit/<num>", methods=['POST', 'GET'])
@admin_only
@login_required
def edit_post(num):
    if request.method == 'POST':
        # Update post data from submitted form and clean HTML content
        post_data = request.form.to_dict()
        post_data.pop('csrf_token')
        post_data.pop('submit_btn')
        post_data['body'] = cleanify(post_data['body'])
        post_data['body'] = html.unescape(post_data['body'])

        # Update post record in DB
        stmt = update(Post).where(Post.id == int(num)).values(**post_data)
        db.session.execute(stmt)
        db.session.commit()
        db.session.close()

        return redirect(url_for('home'))

    else:
        # Pre-fill form with existing post data for editing
        posts = get_blog_data()
        for post in posts:
            if post.id == int(num):
                edit_form = PostForm(
                    title=post.title,
                    subtitle=post.subtitle,
                    date=post.date,
                    img_url=post.img_url,
                    author=post.author,
                    body=post.body
                )
                return render_template('update_post.html',
                                       form=edit_form,
                                       year=current_year,
                                       logged_in=current_user.is_authenticated)


# Run the Flask application with debug mode off (production)
if __name__ == "__main__":
    app.run(debug=False)

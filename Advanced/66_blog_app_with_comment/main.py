from flask import Flask, render_template, request, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, time
from send_mail import GmailSender
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, delete, update, select, ForeignKey
from forms import CommentForm, LoginForm, PostForm, RegisterForm, CKEditor
from flask_ckeditor.utils import cleanify
import html
from functools import wraps
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from typing import List
from flask_gravatar import Gravatar

# Get current year for footer or page info
current_year = datetime.today().year

# -------------------- Flask App Configuration --------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0s'  # Needed for Flask-WTF CSRF protection

# Enable CKEditor for rich text editing
ckeditor = CKEditor(app)

# Enable Bootstrap 5 for styling
Bootstrap5(app)

# --- Flask-Login Configuration ---
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# Tells Flask-Login how to load a user from the session
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# -------------------- Database Configuration --------------------
# Create base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


# SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Bind SQLAlchemy instance to application
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Blog Post table model
class Post(db.Model):
    __tablename__ = "post_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Unique ID
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Blog title
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)  # Blog subtitle
    date: Mapped[str] = mapped_column(String(250), nullable=False)  # Date of the blog
    body: Mapped[str] = mapped_column(Text, nullable=False)  # Blog content
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # Author name
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # Image URL
    author_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship()


class User(db.Model, UserMixin):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    posts: Mapped[List["Post"]] = relationship(back_populates='user')
    comments: Mapped[List["Comment"]] = relationship()

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


class Comment(db.Model):
    __tablename__ = "comment_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(250), nullable=False)
    commentator_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    commentator: Mapped["User"] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))
    post: Mapped["Post"] = relationship(back_populates="comments")


# Create database tables
with app.app_context():
    db.create_all()


# -------------------- Helper Functions --------------------
# Fetch all blog posts from the database
def get_blog_data():
    stmt = select(Post)
    blogs = db.session.execute(stmt).scalars().all()
    return blogs


# Gmail sender instance for sending contact form emails
gs = GmailSender()


# -------------------- Routes --------------------

# Home page - show list of all blog posts
@app.route("/")
def home():
    data = get_blog_data()
    if current_user.is_authenticated:
        id_ = current_user.id
    else:
        id_ = 2
    return render_template(template_name_or_list='index.html',
                           year=current_year,
                           posts=data,
                           logged_in=current_user.is_authenticated,
                           user_id=id_
                           )


@app.route('/register', methods=['POST', "GET"])
def register():
    registerform = RegisterForm()
    if request.method == "POST":
        # Check if user already exists
        stmt = select(User).where(User.email == request.form.get('email'))
        user = db.session.execute(stmt).scalar()
        if user is None:
            user_data = {"name": request.form.get('name'),
                         "email": request.form.get("email"),
                         "password": request.form.get('password')}
            user_data['password'] = generate_password_hash(user_data['password'], method='pbkdf2:sha256', salt_length=8)
            new_user = User(**user_data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
        else:
            flash('This email has been already registered. Login instead.')
            return redirect(url_for('login'))

    return render_template('register.html', form=registerform, logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        stmt = select(User).where(User.email == email)
        user = db.session.execute(stmt).scalar()
        if user is not None:
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# About page
@app.route("/about")
def about():
    return render_template('about.html', year=current_year, logged_in=False)


# Contact page - send email on form submission
@app.route("/contact", methods=['GET', "POST"])
def contact():
    if request.method == 'POST':
        # Collect form data
        form_data = {
            'Name': request.form.get('name'),
            'Email': request.form.get('email'),
            'Phone': request.form.get('phone'),
            'Message': request.form.get('message'),
        }
        # Prepare email body
        details = ""
        for key, value in form_data.items():
            details += f"{key}: {value}\n"

        # Send email using GmailSender class
        gs.send_mail(user_detail=details)
        return render_template('success.html', year=current_year, logged_in=False)

    else:
        return render_template('contact.html', year=current_year, logged_in=False)


# Display a single blog post
@app.route("/post/<int:num>", methods=["POST", 'GET'])
def get_post(num):
    commentform = CommentForm()
    current_post = db.session.execute(select(Post).where(Post.id == num)).scalar()
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
            id_ = 2

        return render_template(template_name_or_list='post.html',
                               post=current_post,
                               comments=all_comments,
                               year=current_year,
                               logged_in=current_user.is_authenticated,
                               user_id=id_,
                               form=commentform,
                               gravatar=gravatar
                               )


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id == 1:
            result = f(*args, **kwargs)
            return result
        else:
            abort(404)

    return decorated_function


# Create a new blog post
@app.route("/newpost", methods=['POST', 'GET'])
@admin_only
@login_required
def create_post():
    if request.method == "POST":
        # Extract form data and clean HTML
        post_data = request.form.to_dict()
        post_data.pop('csrf_token')
        post_data.pop('submit_btn')
        post_data['body'] = cleanify(post_data['body'])
        post_data['body'] = html.unescape(post_data['body'])

        # Insert into DB
        new_post = Post(user=current_user, **post_data)
        print(current_user.posts)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        postform = PostForm()
        return render_template('new_post.html', form=postform, year=current_year,
                               logged_in=current_user.is_authenticated)


# Delete a post by ID
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


# Edit an existing post
@app.route("/edit/<num>", methods=['POST', 'GET'])
@admin_only
@login_required
def edit_post(num):
    if request.method == 'POST':
        # Update post data
        post_data = request.form.to_dict()
        post_data.pop('csrf_token')
        post_data.pop('submit_btn')
        post_data['body'] = cleanify(post_data['body'])
        post_data['body'] = html.unescape(post_data['body'])

        stmt = update(Post).where(Post.id == int(num)).values(**post_data)
        db.session.execute(stmt)
        db.session.commit()
        db.session.close()

        return redirect(url_for('home'))

    else:
        # Pre-fill the form with existing blog data
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
                return render_template('update_post.html', form=edit_form, year=current_year,
                                       logged_in=current_user.is_authenticated)


# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True, port=5002)

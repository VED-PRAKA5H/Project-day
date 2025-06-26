from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date
from send_mail import GmailSender
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, insert, delete, update
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from flask_ckeditor.utils import cleanify
import html

# Get current year for footer or page info
current_year = datetime.today().year

# -------------------- Flask App Configuration --------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0s'  # Needed for Flask-WTF CSRF protection

# Enable CKEditor for rich text editing
ckeditor = CKEditor(app)

# Enable Bootstrap 5 for styling
Bootstrap5(app)


# -------------------- Database Configuration --------------------
# Create base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


# SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# Bind SQLAlchemy instance to application
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Blog Post table model
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Unique ID
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Blog title
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)  # Blog subtitle
    date: Mapped[str] = mapped_column(String(250), nullable=False)  # Date of the blog
    body: Mapped[str] = mapped_column(Text, nullable=False)  # Blog content
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # Author name
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # Image URL


# Create database tables
with app.app_context():
    db.create_all()


# -------------------- Helper Functions --------------------
# Fetch all blog posts from the database
def get_blog_data():
    stmt = db.select(BlogPost)
    blogs = db.session.execute(stmt).scalars().all()
    return blogs


# Gmail sender instance for sending contact form emails
gs = GmailSender()


# -------------------- Flask-WTF Form --------------------
class PostForm(FlaskForm):
    """Form for creating/updating a blog post"""
    title = StringField(label="Enter the title of the blog", validators=[DataRequired()])
    subtitle = StringField(label="Enter the subtitle of the blog", validators=[DataRequired()])
    date = StringField(label="Blog date", validators=[DataRequired()])
    body = CKEditorField(label="Write the content of the blog", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Image link of the blog", validators=[DataRequired(), URL()])
    submit_btn = SubmitField(label="Post the blog")


# -------------------- Routes --------------------

# Home page - show list of all blog posts
@app.route("/")
def home():
    data = get_blog_data()
    return render_template('index.html', year=current_year, posts=data)


# About page
@app.route("/about")
def about():
    return render_template('about.html', year=current_year)


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
        return render_template('success.html', year=current_year)

    else:
        return render_template('contact.html', year=current_year)


# Display a single blog post
@app.route("/post/<num>")
def get_post(num):
    data = get_blog_data()
    return render_template('post.html', posts=data, post_no=int(num), year=current_year)


# Create a new blog post
@app.route("/newpost", methods=['POST', 'GET'])
def create_post():
    if request.method == "POST":
        # Extract form data and clean HTML
        post_data = request.form.to_dict()
        post_data.pop('csrf_token')
        post_data.pop('submit_btn')
        post_data['body'] = cleanify(post_data['body'])
        post_data['body'] = html.unescape(post_data['body'])

        # Insert into DB
        stmt = insert(BlogPost).values(**post_data)
        db.session.execute(stmt)
        db.session.commit()
        db.session.close()

        return redirect(url_for('home'))

    else:
        postform = PostForm()
        return render_template('new_post.html', form=postform, year=current_year)


# Delete a post by ID
@app.route("/delete/<num>", methods=['POST'])
def delete_post(num):
    if request.method == 'POST':
        stmt = delete(BlogPost).where(BlogPost.id == int(num))
        db.session.execute(stmt)
        db.session.commit()
        db.session.close()

    return redirect(url_for('home'))


# Edit an existing post
@app.route("/edit/<num>", methods=['POST', 'GET'])
def edit_post(num):
    method = request.environ.get('override_method', request.method)

    if method == 'POST':
        # Update post data
        post_data = request.form.to_dict()
        post_data.pop('csrf_token')
        post_data.pop('submit_btn')
        post_data['body'] = cleanify(post_data['body'])
        post_data['body'] = html.unescape(post_data['body'])

        stmt = update(BlogPost).where(BlogPost.id == int(num)).values(**post_data)
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
                return render_template('update_post.html', form=edit_form, year=current_year)


# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)

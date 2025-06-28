from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField, CKEditor


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


class LoginForm(FlaskForm):
    """Form for user to login"""
    email = EmailField(label="Enter email", validators=[DataRequired()])
    password = PasswordField(label="Enter the password", validators=[DataRequired()])
    remember = BooleanField(label="Remember me")
    submit_btn = SubmitField(label="Login")


class RegisterForm(FlaskForm):
    """Form for user to login"""
    name = StringField(label='Enter your name', validators=[DataRequired()])
    email = EmailField(label="Enter email", validators=[DataRequired()])
    password = PasswordField(label="Enter the password", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField(label="Remember me")
    submit_btn = SubmitField(label="Sign me up")


class CommentForm(FlaskForm):
    comment = TextAreaField(label="Comment", validators=[DataRequired()])
    submit_btn = SubmitField(label="Submit comment")

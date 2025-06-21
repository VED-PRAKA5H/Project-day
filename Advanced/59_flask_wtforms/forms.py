from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email


class MyForm(FlaskForm):
    # user_name = StringField(label='Name', validators=[DataRequired()])
    user_password = PasswordField(label="Password", validators=[DataRequired(), Length(min=4)])
    user_email = EmailField(label="Email", validators=[DataRequired(), Email(), Length(min=8)])
    submit_btn = SubmitField(label="Log In")


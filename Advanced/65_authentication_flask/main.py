from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select
import os
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# --- Flask-Login Configuration ---
login_manager = LoginManager()
login_manager.init_app(app)


# Tells Flask-Login how to load a user from the session
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class Base(DeclarativeBase):
    """ CREATE DATABASE"""
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model, UserMixin):
    """CREATE TABLE IN DB"""
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['POST', "GET"])
def register():
    if request.method == "POST":
        # Check if user already exists
        stmt = select(User).where(User.email == request.form.get('email'))
        user = db.session.execute(stmt).scalar()
        if user is None:
            user_data = request.form.to_dict()
            user_data['password'] = generate_password_hash(user_data['password'], method='pbkdf2:sha256', salt_length=8)
            new_user = User(**user_data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
        else:
            flash('This email has been already registered. Login instead.')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        stmt = select(User).where(User.email == email)
        user = db.session.execute(stmt).scalar()
        if user is not None:
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Incorrect Password.')
                return render_template('login.html')
        else:
            flash(f'This email is not registered, please register first.')
            return render_template('register.html')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    # Construct the full path to the file
    filename = 'cheat_sheet.pdf'
    full_path = os.path.join(app.root_path, 'static/file')

    return send_from_directory(
        full_path, filename, as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)

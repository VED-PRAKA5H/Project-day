# Flask User Authentication App

A secure user authentication system built with **Flask**, **Flask-Login**, and **SQLAlchemy**. This app enables users to **register**, **login**, and **access protected content**. Passwords are securely hashed with Werkzeug, and all user data is stored in a SQLite database.

***

### Features

- **User registration** with email and password hashing.
- **Login/logout** with session management using Flask-Login.
- **Protected routes** (`@login_required`) for authorized users.
- **Password hashing** (PBKDF2-SHA256).
- **Secure user model** with SQLAlchemy ORM.
- **Downloadable resource** for logged-in users.
- **Flash messages** for authentication feedback.

***

### Project Structure

```text
project/
│
├── app.py               # The main Flask application
├── templates/           # HTML templates (index, login, register, secrets, etc.)
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── secrets.html
├── static/              # Static files (CSS, images, downloadable files)
│   ├── css/             # CSS files for custom styling
│   │   └── styles.css    # Main CSS file
│   ├── file/              # Directory containing downloadable files (e.g., cheat_sheet.pdf)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```


***

### Installation

1. Clone the repository

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

***

### Usage

1. Place `cheat_sheet.pdf` in `static/file/`.

2. Run the app:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

***

### Requirements

Add to `requirements.txt`:
```
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
```


***

### How it Works

- **Register:** New users can register with an email, password, and name. Passwords are stored securely using PBKDF2 hash.[1][2]
- **Login:** Existing users enter credentials to access protected content.
- **Secrets Page:** Only authenticated users can view/download protected resources.
- **Logout:** Users may end their session at any time.

***

### Example Screenshots (Optional)

- Registration page
- Login page
- Secrets page (for logged in users)
- Flash messages for errors and notices

***

### License

MIT License.

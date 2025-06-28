# 📜 Flask Blog Application

A full-featured **Flask-based Blog** application that allows users to create, edit, and delete blog posts, view posts, and send messages via a contact form.  
Built using **Flask**, **Flask-WTF**, **Flask-Bootstrap**, **SQLAlchemy**, and **Flask-CKEditor**.

***

## 🚀 Features

- **Home Page:** View all published blog posts.
- **Single Post Page:** View a specific blog post in detail.
- **Create Post:** Add a new blog post with title, subtitle, body, and image.
- **Edit Post:** Update an existing post using a pre-filled form.
- **Delete Post:** Remove a blog post from the database.
- **Contact Form:** Send messages via email using Gmail.
- **Rich Text Editing:** Powered by CKEditor for blog body.
- **Responsive Design:** Styled with Bootstrap 5.

***

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite (via SQLAlchemy ORM)
- **Forms:** Flask-WTF
- **Rich Text Editor:** Flask-CKEditor
- **Email:** Custom GmailSender class
- **Template Engine:** Jinja2

***

## 📂 Project Structure

```
project/
│-- app.py               # Main Flask application
│-- send_mail.py          # Gmail sender utility
│-- templates/            # HTML templates
│   ├── index.html
│   ├── post.html
│   ├── new_post.html
│   ├── update_post.html
│   ├── contact.html
│   ├── about.html
│   └── success.html
│-- static/               # Static files (CSS, JS, Images)
│-- instance/            
│   └── posts.db          # SQLite database
│-- requirements.txt       # Python dependencies
```

***

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

### 2️⃣ Create a Virtual Environment & Activate
```bash
python -m venv venv
# Windows
venv\Scripts\activate

```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Set your Gmail username & app password in `send_mail.py` or use environment variables:
```python
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
```

Generate an **App Password** from Gmail if 2FA is enabled.

### 5️⃣ Initialize Database
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 6️⃣ Run the Server
```bash
python app.py
```
Visit: **http://127.0.0.1:5000/**

***

## 📋 API / Routes

| Route      | Methods   | Description          |
|------------|-----------|----------------------|
| `/`        | GET       | Home page with blogs |
| `/about`   | GET       | About page           |
| `/contact` | GET, POST | Contact form         |
| `/post/`   | GET       | View single blog     |
| `/newpost` | GET, POST | Create new blog      |
| `/edit/`   | GET, POST | Edit existing blog   |
| `/delete/` | POST      | Delete blog post     |

***

## ✏ Method Override for PUT/DELETE
Since browsers only support **GET** & **POST** in standard forms,  
PUT & DELETE are simulated using:
```html

```
Then Flask handles it via `request.environ.get('override_method', request.method)`.

***

## 📌 Known Improvements
- Integrate flask-method-override middleware for cleaner PUT/DELETE handling.
- Add user authentication for admin features.
- Support image uploads instead of URLs.

***

## 📜 License
This project is licensed under the MIT License.

***
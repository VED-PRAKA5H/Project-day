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
- **User Authentication:** Register, login, logout.
- **Comments:** Authenticated users can comment on posts.

***

## 🛠 Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Database:** SQLite (via SQLAlchemy ORM)  
- **Forms:** Flask-WTF  
- **Rich Text Editor:** Flask-CKEditor  
- **Email:** Custom GmailSender class  
- **Authentication:** Flask-Login  
- **Template Engine:** Jinja2  

***

## 📂 Project Structure

```
project/
│-- main.py                # Main Flask application with routes and models
│-- send_mail.py          # Gmail sender utility class
│-- forms.py              # WTForms classes for user input forms
│-- templates/            # HTML Templates for rendering pages
│   ├── index.html
│   ├── post.html
│   ├── new_post.html
│   ├── update_post.html
│   ├── contact.html
│   ├── about.html
│   └── success.html
│-- static/               # Static files (CSS, JS, Images)
│-- requirements.txt      # Python dependencies
│-- .env                  # Environment variables (not committed)
```

***

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables
Set environment variables required for the app (e.g., in a `.env` file or your OS environment):
- `FLASK_KEY` — Flask secret key for session and CSRF protection
- `DB_URI` — Database connection string (e.g., `sqlite:///blog.db`)
- Gmail credentials/environment (used by `GmailSender` for sending emails)

### 5️⃣ Initialize the Database
```bash
flask shell
>>> from app import db
>>> db.create_all()
```

### 6️⃣ Run the Application
```bash
flask run
```

***

## 🔐 Admin Access

- The first registered user (with ID = 1) is considered the admin.
- Admin-only access is required to create, edit, and delete blog posts.

***

## 📝 Usage

- Register a new user at `/register`.
- Login via `/login`.
- View all posts on the homepage `/`.
- Click on a post title to view detailed post page with comments.
- Admin can create new posts at `/newpost`.
- Admin can edit or delete posts from respective post pages.
- Use `/contact` to send a message via email.

***

## ⚙️ Environment Variables Example (.env)

```env
FLASK_KEY=your_secret_key_here
DB_URI=sqlite:///blog.db
GMAIL_USER=your-email@gmail.com
GMAIL_PASSWORD=your-app-password
```

***

## 📫 Contact

For issues or contributions, please open an issue or pull request.

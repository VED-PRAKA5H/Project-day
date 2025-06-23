# 📚 Flask Library App

A minimal web app to manage your personal library using **Flask** + **SQLite** + **SQLAlchemy**.  
You can **add books, view all books, and update their ratings**.  

---

## 🚀 Features
- View all books in your library
- Add a new book with author and rating
- Update rating of existing books
- SQLite database in `/instance/books.db`
- Minimal clean UI with shared CSS

---

## 📂 Project Structure
```text
flask_library_app/
│
├── app.py                 # Main Flask app (routes + logic)
├── db_stuff.py           # Database config, Book model, and CRUD functions
├── requirements.txt       # Python dependencies
├── /templates/            # HTML templates (index, add, update)
│   ├── index.html
│   ├── add.html
│   └── update.html
├── /static/
│   └── styles.css         # Minimal shared CSS
└── /instance/
    └── books.db           # SQLite database file (auto-created if missing)
```

---

## 🛠 Installation

### 1️⃣ Clone the repository
```
git clone https://github.com/yourusername/flask-library-app.git
cd flask-library-app
```

### 2️⃣ Create virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

---

## 📦 requirements.txt
```
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.32
```
*(Flask-WTF can be added if you integrate it later)*

---

## ▶ Running the App

### 1️⃣ Ensure the `/instance` folder exists  
This is where Flask will store `books.db`. Create it if missing:

```
mkdir instance
```

### 2️⃣ Start the server:
```
python app.py
```

The app will run locally at:  
📌 `http://127.0.0.1:5000/`

---

## 💾 Database Notes
- The SQLite database file is stored in `/instance/books.db`
- Tables are auto-created on first run if missing.

---

## 📜 Example Usage
1. Visit the home page — see all your books.
2. Click "➕ Add New Book" to add a new book.
3. Click "✏ Update Rating" on any book to change its rating.

---

## 🧑‍💻 Development Tips
- Modify `static/styles.css` to change the theme.
- Keep `/instance/books.db` if you want to persist records between runs.
- Delete `/instance/books.db` and restart the app if you want a fresh database.

---

**Author:** Ved Prakash
**License:** MIT

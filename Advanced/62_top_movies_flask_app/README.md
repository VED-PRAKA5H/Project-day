# 🎬 Movie Collection App  
A Flask web application to manage your personal movie collection — search for movies from **TMDB** (The Movie Database) API, save them locally using SQLite, and update ratings/reviews.  

***

## 📌 Features
- 🔍 Search movies from TMDB API & select the desired one.
- 💾 Save movies to a local **SQLite** database via SQLAlchemy ORM.
- ✏️ Edit movie ratings and reviews.
- 📊 Automatically rank movies based on ratings.
- 🗑️ Delete unwanted movies from the collection.
- 🎨 Styled using **Bootstrap 5** for a modern look.

***

## 🛠️ Tech Stack
- **Flask** – Web framework
- **Flask-WTF** – Form handling
- **Flask-Bootstrap5** – UI styling
- **SQLAlchemy** – ORM for database operations
- **SQLite** – Local database
- **TMDB API** – Movie data source
- **WTForms** – Form validation
- **Requests** – HTTP API calls

***

## 📂 Project Structure
```
project/
│
├── main.py                 # Main Flask app with routes
├── movies_db.py            # Database models & service functions
├── movie_api.py            # TMDB API integration
├── templates/              # HTML templates (index, add, edit, select)
├── static/                 # Static assets (CSS, JS, images)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (TMDB API key)
└── README.md               # Project documentation
```

***

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set up Environment Variables**
Create a `.env` file in the project root:
```env
TMDB_API=your_tmdb_api_key_here
```
> Get your TMDB API key from [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

### **5️⃣ Run the Application**
```bash
python app.py
```
- App runs at: **http://127.0.0.1:5000/**

***

## 🚀 Usage
1. Visit the homepage to see your movie collection.
2. Click **"Add Movie"** → Search for a movie title.
3. Select the desired movie from the TMDB results.
4. Enter your rating & review.
5. Movies are automatically ranked based on ratings.
6. Edit or delete movies anytime.

***

## 📌 API Notes
- Movie search is powered by **TMDB API**.
- Image URLs are constructed using TMDB's base image URL.
- Only public TMDB API access is required (free tier).

***

## 🐛 Known Issues
- `tmdb_movies` is stored in a **global list** — will reset if the server restarts.  
- No pagination for search results.

***

## 🔮 Future Improvements
- Store TMDB search results in a temporary database table.
- Add user authentication.
- Support movie poster uploads.
- Deploy on **Heroku / Render** with persistent DB.

***

## 📜 License
This project is open-source under the **MIT License**.


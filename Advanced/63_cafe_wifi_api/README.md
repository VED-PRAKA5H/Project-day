# ☕ Cafe & WiFi API

A RESTful API built with **Flask** and **SQLAlchemy** to manage cafes, their locations, facilities, and coffee prices.  
This API allows clients to **view, search, add, update, and delete cafe records**.

***

## 📄 API Documentation

Interactive API documentation is available via Postman:  
**[View Full API Docs here](https://documenter.getpostman.com/view/47569016/2sB3BGHpnx)**

***

## 🚀 Features

- **GET** → Retrieve all cafes, a random cafe, or search by location
- **POST** → Add a new cafe (API key required)
- **PATCH** → Update coffee prices for an existing cafe
- **DELETE** → Remove (report closed) cafes from the database
- SQLite database for easy local development

***

## 🛠 Tech Stack

- **Flask** — Python micro web framework
- **Flask-SQLAlchemy** — ORM for database interaction
- **SQLite** — Lightweight local DB
- **SQLAlchemy Core** for Insert/Update/Delete statements
- **Postman** (for API documentation & testing)

***

## 📂 Project Structure

```
Cafe-WiFi-API/
│
├── app.py              # Main Flask application with routes
├── templates/
│   └── index.html      # Home page with API link
├── instance/
│   └── cafes.db        # SQLite database (auto-created if missing)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

***

## ⚙ Installation & Setup

1️⃣ **Clone the repository**

2️⃣ **Create a virtual environment & activate it**
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Run the Flask app**
```bash
python app.py
```

5️⃣ **Access in browser or Postman**  
- Home Page: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
- API endpoints as documented below.

***

## 🔌 API Endpoints

### **1. Get a Random Cafe**
`GET /random`
```bash
curl http://127.0.0.1:5000/random
```

### **2. Get All Cafes**
`GET /all`

### **3. Search Cafes by Location**
`GET /search?loc=`

### **4. Add a New Cafe** *(Requires `api-key` in query param)*
`POST /add?api-key=TopSecretAPI987686`
- Body (JSON):
```json
{
  "name": "Timberyard",
  "map_url": "https://maps.example.com",
  "img_url": "https://images.example.com",
  "location": "Soho",
  "has_toilet": true,
  "has_wifi": true,
  "has_sockets": true,
  "can_take_calls": true,
  "coffee_price": "₹10",
  "seats": "20-30"
}
```

### **5. Update Coffee Price**
`PATCH /update-price/?new_price=₹15`

### **6. Delete a Cafe** *(Requires `api-key` in request header)*
`DELETE /report-closed/`
- Headers:
```
api-key: abcd1234
```

***

## 🔐 API Key Requirements
| Action        | API Key Location | Example Key           |
|---------------|------------------|-----------------------|
| Add Cafe      | Query Parameter  | TopSecretAPI987686    |
| Delete Cafe   | Request Header   | abcd1234              |

***

## 🗄 Database

- SQLite database file `cafes.db` is auto-created on first run.
- Schema:
  - `id` (Integer, Primary Key)
  - `name` (String, Unique)
  - `map_url`, `img_url`, `location`, `seats`
  - `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls` (Boolean)
  - `coffee_price` (String)

***

## 👨💻 Author

**Ved Prakash**
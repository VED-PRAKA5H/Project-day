# 🏋️‍♂️ Exercise Tracker App  
Log your workouts using the **Nutritionix API** and save them in a Google Sheet via **Sheety**. Just describe your exercises in plain English—this app takes care of the rest.

### 🚀 Prerequisites

- `.env` file with these variables:
  - `NUTRITIONIX_APP_ID`
  - `NUTRITIONIX_API_KEY`
  - `SHEETY_AUTH_KEY`
  - `SHEET_ID`
- **Required Libraries**  
  Install via pip:
  ```bash
  pip install requests python-dotenv
  ```

### 🧩 APIs Used

- **[Nutritionix](https://www.nutritionix.com/business/api):**
  Natural language exercise interpretation and calorie estimation

- **[Sheety](https://sheety.co/)**: 
  Easily send data to your Google Sheet

### 📝 Features

- Accepts natural language input like:  
  `"I did 30 minutes of yoga and ran 3 km."`

Enter your workout when prompted, and it will be logged to your Google Sheet automatically.

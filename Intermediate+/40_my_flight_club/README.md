# 🛫 My Flight Club
Get notified about the cheapest round-trip flight deals from your origin city to multiple destinations using the Amadeus API, Google Sheets, and SMTP email notifications.

### 🔧 Prerequisites
- **Amadeus for Developers** - Flight data API access ([developers.amadeus.com](https://developers.amadeus.com))  
- **Sheety (Google Sheets API)** - Manage flight and user data ([sheety.co](https://sheety.co))  
- **SMTP** - Send email notifications  
- **Python 3.8+** - Required packages: `requests`, `python-dotenv`, `smtp`
- Create a `.env` file in the root directory and add your credentials:
   ```env
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_APP_SECRET=your_amadeus_secret
   FLIGHT_SHEET_ID=your_sheety_project_id
   FLIGHT_SHEETY_AUTH_KEY=your_sheety_auth_key
   EMAIL_PASSWORD=your_email_password
   ```

### 🚀 Usage
- **Sign up for alerts:**  
  Fill out your details using this [Google Form](https://forms.gle/fvJ5BRa) to receive flight notifications.

### ✨ Features
- It's an Updated Version of **Project 39**
- Authenticates and fetches flight data from Amadeus API  
- Searches for direct flights; falls back to connecting flights if needed  
- Stores and updates flight data in Google Sheets via Sheety  
- Finds the cheapest round-trip flights within a 6-month window  
- Sends low-price alerts via email using SMTP


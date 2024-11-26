# 🛫 Flight Deal Alert System

Track and get notified about the cheapest flight deals from your origin city to multiple destinations using Amadeus API, Google Sheets, and Twilio SMS notifications.

### Prerequisites

* **Amadeus for Developers:** [https://developers.amadeus.com](https://developers.amadeus.com) — for flight data API access  
* **Google Sheets API via Sheety:** [https://sheety.co](https://sheety.co) — to manage flight data in a spreadsheet  
* **Twilio:** [https://www.twilio.com](https://www.twilio.com) — to send SMS notifications  
* **Python 3.8+** with the following packages: `requests`, `python-dotenv`, `twilio`

### Setup & Installation

- Create a `.env` file in the root directory and add your API keys and credentials:
   ```
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_APP_SECRET=your_amadeus_secret
   FLIGHT_SHEET_ID=your_sheety_project_id
   FLIGHT_SHEETY_AUTH_KEY=your_sheety_auth_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   MY_PHONE=your_phone_number
   SENDER_PHONE=your_twilio_phone_number
   ```
   
### Usage

- **Update IATA Codes:**  
  Run the `update_iata()` function to fetch and update IATA codes for your cities in the Google Sheet.

- **Check Flight Prices and Send Notifications:**  
  Run the `update_price()` function to search for the cheapest flights over the next 6 months, update your sheet with new prices, and send SMS alerts for the best deals.


### Features

- Fetches flight data from Amadeus API with authentication handling  
- Stores and updates flight data in Google Sheets via Sheety API  
- Finds the cheapest round-trip flights within a 6-month window  
- Sends SMS notifications about low price alerts using Twilio  


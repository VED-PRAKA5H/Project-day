# Amazon Price Tracker
Track the price of product listed on Amazon.com using BeautifulSoup

## 🔧 Prerequisites
- **Beautiful soup** scrape the price of product —  
- **headers** — Get your headers ([https://httpbin.org/headers](https://httpbin.org/headers))  
- **SMTP** — Send email notifications  
- **Python ** — Required packages: `requests`, `python-dotenv`, `smtp`
- Create a `.env` file in the root directory and add your credentials:
   ```env
   SENDER_EMAIL
   RECEIVER_EMAIL
   EMAIL_PASSWORD=your_email_password
   ```

## ✨ Features
- Track the price of product
- Fetches product price using beautifulsoup
- Sends low-price alerts via email using SMTP if price is lower than certain limit


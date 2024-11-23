import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta

# Get today's date and compute the day before yesterday
now = datetime.now()
yesterday_date = now.date() - timedelta(days=3)

# Load environment variables from the .env file
load_dotenv()

# Fetch API keys and credentials
news_api = os.getenv("NEWS_API_KEY")
stock_api = os.getenv("ALPHAVANTAGE_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_phone = os.getenv("MY_PHONE")
sender = os.getenv("SENDER_PHONE")

# Configuration
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Fetch recent stock data from Alpha Vantage
stock_url = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api,
    "outputsize": 2
}

stock_response = requests.get(url=stock_url, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
day_keys = list(stock_data["Time Series (Daily)"].keys())

# Get closing prices for the last two days
yesterday_close = float(stock_data["Time Series (Daily)"][day_keys[0]]["4. close"])
day_before_close = float(stock_data["Time Series (Daily)"][day_keys[1]]["4. close"])

# Calculate stock movement percentage
if yesterday_close > day_before_close:
    change = ((yesterday_close - day_before_close) * 100) / day_before_close
    stock_status = f"🔼🔺 {change:.2f}%"
else:
    change = ((day_before_close - yesterday_close) * 100) / day_before_close
    stock_status = f"🔽🔻{change:.2f}%"

# STEP 2: Fetch news about the company using News API
news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday_date,
    "to": now.date(),
    "sortBy": "popularity",
    "searchIn": "description",
    "apiKey": news_api
}

news_response = requests.get(url=news_url, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

# Format messages for SMS
news_list = []
for article in news_data["articles"][:3]:
    full_news = (
        f"{STOCK} {stock_status}\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
    )
    news_list.append(full_news)


# STEP 3: Send SMS using Twilio
client = Client(account_sid, auth_token)
try:
    for news in news_list:
        if len(news) > 150:
            message1 = client.messages.create(
                body=news[:150],
                from_=sender,
                to=my_phone,
            )
            message2 = client.messages.create(
                body=news[150:],
                from_=sender,
                to=my_phone,
            )
            print(f"Message has been sent: {message2.status}\n{message1.body} {message2.body}")
        else:
            message = client.messages.create(
                body=news,
                from_=sender,
                to=my_phone,
            )
            print(f"Message has been sent: {message.status}\n{message.body}")
except Exception as e:
    print(f"Message could not be sent.\n{e}")

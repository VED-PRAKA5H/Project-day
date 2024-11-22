import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from the .env file
load_dotenv()

# Fetch API keys and configuration values from environment variables
weather_api = os.getenv("OPENWEATHERMAP_API_KEY")
lat = os.getenv("LATITUDE")
long = os.getenv("LONGITUDE")
my_phone = os.getenv("MY_PHONE")
sender = os.getenv("SENDER_PHONE")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio Account SID
auth_token = os.getenv("TWILIO_AUTH_TOKEN")    # Twilio Auth Token

# Define parameters for the OpenWeatherMap API request
parameters = {
    "lat": lat,
    "lon": long,
    "appid": weather_api,
    # "lang": "hi",  # Optional: Set language for response
    "cnt": 5,  # Number of forecast intervals (each interval is 3 hours apart)
}

# -------------------------Retrieve forecast weather data-------------------------
three_hour_url = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=three_hour_url, params=parameters)
response.raise_for_status()
results = response.json()

# Set default weather update
update = "It's a clear sky 🌞."

# Analyze weather conditions from forecast data
for weathers in results["list"]:
    weather_id = weathers["weather"][0]["id"]
    if 500 <= weather_id < 700:
        update = "It will rain ☔."
        break  # No need to check further if rain is expected
    elif weather_id > 700:
        update = "It's cloudy today ⛅."

# -------------------------Send SMS via Twilio-------------------------
client = Client(account_sid, auth_token)
try:
    message = client.messages.create(
        body=f"Good Morning! {update}",
        from_=sender,
        to=my_phone,
    )
    print(f"Message has been sent: {message.status}.\n{message.body}")
except Exception as e:
    print(f"Message could not be sent.\n{e}")



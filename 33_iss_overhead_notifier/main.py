import os
import time
import smtplib
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("SENDER_EMAIL")
my_password = os.getenv("PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

MY_LAT = 25.3356491  # Your latitude
MY_LONG = 83.0076292  # Your longitude

def is_iss_near_me():
    try:
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
        iss_response.raise_for_status()
        iss_data = iss_response.json()

        iss_latitude = float(iss_data["iss_position"]["latitude"])
        iss_longitude = float(iss_data["iss_position"]["longitude"])

        return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5
    except Exception as e:
        print(f"Error checking ISS location: {e}")
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
        response.raise_for_status()
        data = response.json()

        sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        now_utc = datetime.now(timezone.utc).hour
        return now_utc < sunrise_hour or now_utc > sunset_hour
    except Exception as e:
        print(f"Error checking sunrise/sunset data: {e}")
        return False

def send_alert():
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_email,
                msg="Subject: Look up!\n\nThe ISS is overhead and it's dark enough to see it. Go outside and enjoy the view!"
            )
            print("Email sent! 🚀")
    except Exception as e:
        print(f"Error sending email: {e}")

# Run every 60 seconds
count = 0
while True:
    print("Checking ISS position and visibility...")
    if is_dark() and is_iss_near_me():
        send_alert()
    else:
        count += 1
        print("Not near: ", count)
    time.sleep(60)

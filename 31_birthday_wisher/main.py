import os
import random
import smtplib
import pandas as pd
import datetime as dt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Validate credentials
if not my_email or not password:
    raise ValueError("Missing EMAIL or PASSWORD in environment variables.")


def send_wish(email, letter):
    """Send the birthday email using Gmail SMTP server.
        Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    """
    message = f"Subject: Happy Birthday 🎉\n\n{letter}"
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)
    except smtplib.SMTPException as e:
        print(f"Failed to send email to {email}: {e}")


# Get today's date
today = dt.datetime.now()

# Read birthday data
try:
    data = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Error: 'birthdays.csv' not found.")
    exit()

# Check and send birthday wishes
for _, row in data.iterrows():
    if today.day == row["day"] and today.month == row["month"]:
        try:
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
                content = file.read()
            personalized = content.replace("[NAME]", row["name"])
            send_wish(row["email"], personalized)
        except FileNotFoundError:
            print("Error: Letter template file not found.")

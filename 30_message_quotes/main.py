import os
import random
import smtplib
from dotenv import load_dotenv
import datetime as dt

now = dt.datetime.now()
weekday_no = now.weekday()

week_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday", }

with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    quote = random.choice(quotes).replace('"', "")

message = f"Subject:Quote of the {week_dict[weekday_no]}\n\n{quote}"

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email,
                     password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ved@gmail.com",
                        msg=message
                        )

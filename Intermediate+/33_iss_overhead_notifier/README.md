# ISS Tracker

A Python program to track the International Space Station (ISS) location relative to your position and send an email alert when the ISS is near you during night time, so you can spot it in the sky.

***

### Features
- Uses [ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) to fetch real-time latitude and longitude of the ISS.  
- Uses [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine if it is currently dark at your location.  
- Sends email notifications via Gmail SMTP when ISS is overhead at night.  
- Runs as a continuous background process checking every 60 seconds.  
- Environment variables store email credentials and recipient information securely.

***

### Requirements
- Python 3.x  
- Packages: `requests`, `python-dotenv`

Install via pip:

```bash
pip install requests python-dotenv
```

***

### Setup

1. Create a `.env` file with your email configuration and receiver email:

```
SENDER_EMAIL=your_email@gmail.com
PASSWORD=your_email_password_or_app_password
RECEIVER_EMAIL=receiver_email@example.com
```

2. Update your approximate latitude and longitude coordinates in the script (`MY_LAT`, `MY_LONG`).

***

### How to Run

Run the script:

```bash
python iss_tracker.py
```

- The program will check every minute if the ISS is within 5 degrees latitude and longitude from your location and it is currently dark outside.  
- If conditions are met, it sends an email alert to your specified email address.  
- Prints status logs for checks and email sending.

***

### Code Overview

- `is_iss_near_me()` fetches current ISS location and compares with your coordinates (within ±5 degrees).  
- `is_dark()` uses sunrise-sunset API to determine if current UTC hour is before sunrise or after sunset.  
- `send_alert()` sends email via Gmail SMTP securely using TLS.  
- Continuous loop runs checks every 60 seconds.

***

### Security Notes

- Use app-specific passwords for Gmail if 2FA is enabled.  
- Keep `.env` file private and excluded from version control.  
- Never hardcode passwords in the script.

***

### References

- [ISS Location API Documentation](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)  
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)  
- [Python smtplib Documentation](https://docs.python.org/3/library/smtplib.html)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

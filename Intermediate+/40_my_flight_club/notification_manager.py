import os
from dotenv import load_dotenv
import smtplib

# Load environment variables from a .env file into the system environment
load_dotenv()


class NotificationManager:
    """
    This class is responsible for sending notifications containing flight deal details
    via SMTP email messaging system.
    """

    def __init__(self):
        # Retrieve the sender email address from environment variables
        self.sender_email = os.getenv("SENDER_EMAIL")
        # Retrieve account password from environment variables (used for authentication)
        self.email_password = os.getenv("EMAIL_PASSWORD")

    def send_notification(self, fname: str, lname: str, email: str, update: str):
        """
        Send an email notification with the provided message text.

        Parameters:
        - fname: first name,
        - lname: last name,
        - email: address where notification to be sent
        - update (str): The message string containing flight deal details to be sent.
        """
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.sender_email, password=self.email_password)
                connection.sendmail(
                    from_addr=self.sender_email,
                    to_addrs=email,
                    msg=f"Subject: Flight Offer!\n\nDear {fname} {lname},\n{update}".encode("utf-8")
                )
                print(f"Email sent! 🚀 to {fname}")
        except Exception as e:
            print(f"Error sending email: {e}")

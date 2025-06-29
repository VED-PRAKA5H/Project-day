import os
from dotenv import load_dotenv
import smtplib

# Load environment variables from a .env file into the system environment
load_dotenv()


class GmailSender:
    """
    This class is responsible for sending notifications containing users information singed for news
    via SMTP email messaging system.
    """

    def __init__(self):
        # Retrieve the sender email address from environment variables
        self.sender_email = os.getenv("SENDER_EMAIL")
        # Retrieve account password from environment variables (used for authentication)
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_receiver = os.getenv("RECEIVER_EMAIL")

    def send_mail(self, user_detail: str):
        """
        Send an email notification with the provided message text.

        Parameters:
        - user_detail: users information,
        """
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.sender_email, password=self.email_password)
                connection.sendmail(
                    from_addr=self.sender_email,
                    to_addrs=self.email_receiver,
                    msg=f"Subject: New Message!\n\nDear Ved,\n{user_detail}".encode("utf-8")
                )

        except Exception as e:
            raise f"Error sending email: {e}"

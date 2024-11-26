import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from a .env file into the system environment
load_dotenv()


class NotificationManager:
    """
    This class is responsible for sending notifications containing flight deal details
    via SMS using the Twilio API.
    """

    def __init__(self):
        # Retrieve the recipient phone number from environment variables
        self.my_phone = os.getenv("MY_PHONE")
        # Retrieve the Twilio sender phone number from environment variables
        self.sender = os.getenv("SENDER_PHONE")
        # Retrieve Twilio Account SID from environment variables (used for authentication)
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        # Retrieve Twilio Auth Token from environment variables (used for authentication)
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    def send_notification(self, update: str):
        """
        Send an SMS notification with the provided message text.

        Parameters:
        - update (str): The message string containing flight deal details to be sent.
        """
        # Initialize Twilio client with account credentials
        client = Client(self.account_sid, self.auth_token)
        try:
            # Create and send the SMS message
            message = client.messages.create(
                body=f"Good Morning! {update}",  # Message content with a greeting prefix
                from_=self.sender,  # Sender's Twilio phone number
                to=self.my_phone,  # Recipient's phone number
            )
            # Print confirmation with message status and body
            print(f"Message has been sent: {message.status}.\n{message.body}")
        except Exception as e:
            # Handle exceptions such as network errors or invalid credentials
            print(f"Message could not be sent.\n{e}")

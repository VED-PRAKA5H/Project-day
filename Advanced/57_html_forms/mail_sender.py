import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from a .env file into the system environment
load_dotenv()


# Example user_detail dictionary converted to HTML string
def format_user_detail_html(user_detail):
    """
    user_detail: dict with user data (key-value pairs)
    Returns a formatted HTML string for email body
    """
    html_content = """
    <html>
    <head>
        <style>
            body {font-family: Arial, sans-serif; color: #333;}
            h2 {color: #667eea;}
            table {width: 100%; border-collapse: collapse;}
            td, th {padding: 8px 12px; border-bottom: 1px solid #ddd;}
            th {background-color: #764ba2; color: white; text-align: left;}
        </style>
    </head>
    <body>
        <h2>New Registration Details</h2>
        <p>Dear Ved,</p>
        <p>A new user has submitted the registration form. Here are their details:</p>
        <table>
            <tbody>
    """

    # user_detail is expected as dict here (convert if needed)
    for key, value in user_detail.items():
        # Change underscores to spaces & capitalize keys for display
        formatted_key = key.replace('_', ' ').title()
        # Escape or convert None to empty string if needed
        display_value = value if value else ""
        # If value is a list (like interests), join with commas
        if isinstance(display_value, list):
            display_value = ", ".join(display_value)
        html_content += f"<tr><th>{formatted_key}</th><td>{display_value}</td></tr>"

    html_content += """
            </tbody>
        </table>
        <p>Best regards,<br>Your Registration System</p>
    </body>
    </html>
    """
    return html_content


class GmailSender:
    """
    This class is responsible for sending notifications containing users information signed up for news
    via SMTP email messaging system.
    """

    def __init__(self):
        # Retrieve the sender email address from environment variables
        self.sender_email = os.getenv("SENDER_EMAIL")
        # Retrieve account password from environment variables (used for authentication)
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_receiver = os.getenv("RECEIVER_EMAIL")

    def send_mail(self, user_detail: dict, subject: str = "New User Registration"):
        """
        Send an email notification with the provided user details.

        Parameters:
        - user_detail: users information (dict)
        - subject: email subject line
        """
        try:
            # Create message container
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = self.email_receiver

            # Create HTML part
            html_body = format_user_detail_html(user_detail)
            html_part = MIMEText(html_body, 'html')
            msg.attach(html_part)

            # Send email
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.sender_email, password=self.email_password)
                connection.sendmail(
                    from_addr=self.sender_email,
                    to_addrs=self.email_receiver,
                    msg=msg.as_string()
                )
            print("Email sent successfully!")

        except Exception as e:
            raise Exception(f"Error sending email: {e}")


if __name__ == "__main__":
    gs = GmailSender()

    # sample test
    user_detail_dict = {
        'first_name': 'Ram',
        'last_name': 'Dev',
        'email': 'Ram@example.com',
        'phone': '+91123451xxxx',
        'interests': ['technology', 'music']
    }
    gs.send_mail(user_detail=user_detail_dict)

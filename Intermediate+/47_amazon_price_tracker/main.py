import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

# Load environment variables from a .env file (safe way to store credentials)
load_dotenv()

# Get email credentials and receiver address from environment variables
sender_email = os.getenv("SENDER_EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")


def get_price_of_product(product_link):
    """Get the current price of a product from its Amazon page.

    Args:
        product_link (str): Amazon product URL.

    Returns:
        tuple: (product price as float, product title as string), or error message if blocked.
    """
    # Define headers to make request look like it's coming from a regular browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.com/",
        "Connection": "keep-alive"
    }

    # Send GET request to the product page with browser headers
    response = requests.get(url=product_link, headers=headers)
    contents = response.text

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(markup=contents, features="html.parser")

    # Find the price block on the Amazon product page
    price_span = soup.find(name="span", class_="a-price aok-align-center")

    if price_span is not None:
        # Get the actual price value (visible text)
        price_tag = price_span.select_one(selector=".a-offscreen")
        price = price_tag.getText().strip()[1:]  # Remove the currency symbol
        # Get product title using its unique id
        product_title = soup.find(name="span", id="productTitle")
        return float(price.split(" ")[0]), product_title.text.strip()  # Return price(float), title(str)
    else:
        # If price_span is None, request may have been blocked or product info is not found
        return "Amazon blocked the request"


def send_email(message: str):
    """Send an email with the product price info using SMTP (e.g., Gmail SMTP).

    Args:
        message (str): Text content of the email to be sent.
    """
    try:
        # Establish connection to Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure the connection
            connection.login(sender_email, password=email_password)  # Log in to your email account
            # Build and email the recipient
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=f"Subject: Amazon Price Alert!\n\nDear VED,\n{message}".encode("utf-8")
            )
            print(f"Email sent! 🚀 to VED")
    except Exception as e:
        print(f"Error sending email: {e}")


# Main code:
product_url = "https://www.amazon.in/dp/B00ATUZVA0?ref=cm_sw_r_cp_ud_dp_MHY49YJTZG3C09XNPFE9"
product_price, title = get_price_of_product(product_link=product_url)
print(f"Found the product at ₹{product_price} - {title}")

# Prepare the notification message for the email
notification = f"{title} is now ₹{product_price}.\n {product_url}"

# If the price is below a certain threshold (e.g., ₹260), send an alert email
if product_price < 260:
    send_email(message=notification)

from datetime import datetime
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
USER = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph2"

# Base URLs and headers
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs"
HEADERS = {"X-USER-TOKEN": TOKEN}

def create_account():
    """Create a Pixela user account (run once)."""
    user_parameters = {
        "token": TOKEN,
        "username": USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
    return response.text

def create_graph():
    """Create a graph for tracking activity (run once)."""
    graph_config = {
        "id": GRAPH_ID,
        "name": "My Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
    return response.text

def post_pixel(kms_run: float):
    """Post a pixel with today's date and run quantity."""
    today = datetime.now().strftime("%Y%m%d")
    pixel_data = {"date": today, "quantity": str(kms_run)}
    pixel_creation_url = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
    response = requests.post(url=pixel_creation_url, json=pixel_data, headers=HEADERS)
    return response.text

def update_pixel(new_quantity: float):
    """Update the pixel data for today."""
    today = datetime.now().strftime("%Y%m%d")
    pixel_update_url = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{today}"
    response = requests.put(url=pixel_update_url, json={"quantity": str(new_quantity)}, headers=HEADERS)
    return response.text

def delete_pixel():
    """Delete today's pixel data."""
    today = datetime.now().strftime("%Y%m%d")
    delete_url = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{today}"
    response = requests.delete(url=delete_url, headers=HEADERS)
    return response.text

# ---------- Example Calls Below (Uncomment to use) ----------
# print(create_account())
# print(create_graph())
kms_today = input("How many kilometers did you run today? ")
print(post_pixel(float(kms_today)))
# print(update_pixel(new_quantity=1.0))
# print(delete_pixel())

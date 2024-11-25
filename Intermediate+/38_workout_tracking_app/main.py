import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Nutritionix API credentials
nutritionix_app_id = os.getenv("NUTRITIONIX_APP_ID")
nutritionix_api_key = os.getenv("NUTRITIONIX_API_KEY")

# Sheety API credentials
sheety_auth_key = os.getenv("SHEETY_AUTH_KEY")
sheet_id = os.getenv("SHEET_ID")
sheet_name = "myWorkouts"

# Nutritionix API setup
nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key,
}

# Capture exercise input from user
user_input = input("Tell me which exercises you did: ")
nutritionix_parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 165,
    "age": 23
}

# Send data to Nutritionix and get response
response = requests.post(
    url=nutritionix_url,
    headers=nutritionix_headers,
    json=nutritionix_parameters
)
exercises = response.json()["exercises"]

# Get current timestamp
now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

# Sheety endpoint setup
sheety_endpoint = f"https://api.sheety.co/{sheet_id}/{sheet_name}/workouts"
sheety_headers = {
    "Authorization": sheety_auth_key
}

# Add each exercise to Sheety
for exercise in exercises:
    workout_entry = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["user_input"],
            "duration": str(exercise["duration_min"]),
            "calories": str(exercise["nf_calories"])
        }
    }

    sheety_response = requests.post(
        url=sheety_endpoint,
        headers=sheety_headers,
        json=workout_entry
    )

    print("\nAdded row:\n", sheety_response.json())

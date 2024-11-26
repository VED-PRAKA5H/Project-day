import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class DataManager:
    """
    This class is responsible for interacting with a Google Sheet via the Sheety API.
    It handles fetching data from and updating data to the sheet.
    """

    def __init__(self):
        # Get the Sheety project ID (part of the URL) from environment variables
        self.sheet_id = os.getenv("FLIGHT_SHEET_ID")
        # Get the authorization key/token for Sheety API from environment variables
        self.auth_key = os.getenv("FLIGHT_SHEETY_AUTH_KEY")
        # Construct the Sheety API endpoint URL for accessing the "prices" sheet
        self.sheet_end_point = f"https://api.sheety.co/{self.sheet_id}/flightDeals/prices"
        # Prepare the headers with the authorization key for API requests
        self.headers = {"Authorization": self.auth_key}

    def update_cell(self, row_id, column, value):
        """
        Update a specific cell in the Google Sheet.

        Parameters:
        - row_id (int or str): The row number or ID to update in the sheet
        - column (str): The column name/key to update (e.g., 'iataCode', 'lowestPrice')
        - value: The new value to set in the specified cell

        Returns:
        - JSON response from the API if successful, otherwise raw response text
        """
        # Construct the URL to update a specific row by its ID
        update_endpoint = f"{self.sheet_end_point}/{row_id}"
        # Prepare the request body with the column and new value under "price" key
        body = {
            "price": {
                column: value,
            }
        }

        # Send a PUT request to update the cell
        r = requests.put(url=update_endpoint, headers=self.headers, json=body)
        try:
            # Try to parse and return the JSON response
            return r.json()
        except Exception as e:
            # If JSON parsing fails, return the raw response text for debugging
            return r.text

    def get_sheet_data(self):
        """
        Fetch all data from the "prices" sheet.

        Returns:
        - Parsed JSON data containing the sheet's content if successful,
          otherwise raw response text.
        """
        # Send a GET request to retrieve all rows from the sheet
        response = requests.get(url=self.sheet_end_point, headers=self.headers)
        try:
            # Try to parse and return the JSON response
            return response.json()
        except Exception as e:
            # If JSON parsing fails, return the raw response text for debugging
            return response.text

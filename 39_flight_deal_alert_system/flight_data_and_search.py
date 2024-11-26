import os
from dotenv import load_dotenv
import requests
from datetime import timedelta

# Load environment variables from a .env file
load_dotenv()

# API endpoints for Amadeus test environment
AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"  # URL to get OAuth2 access token
FLIGHT_OFFERS_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"  # URL to search flight offers
CITY_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"  # URL to search cities and airports


class FlightData:
    """
    This class is responsible for interacting with the Amadeus API to fetch flight data,
    including authentication, searching flights, and finding the cheapest flights.
    """

    def __init__(self):
        # Initialize token to None; will be set after authentication
        self.token = None
        # Load API credentials from environment variables
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_secret = os.getenv("AMADEUS_APP_SECRET")
        # Obtain access token immediately upon instantiation
        self.get_access_token()

    def get_access_token(self):
        """
        Authenticate with the Amadeus API to get an OAuth2 access token.
        This token is required for subsequent API requests.
        """
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",  # OAuth2 client credentials grant type
            "client_id": self.amadeus_api_key,  # API key (client ID)
            "client_secret": self.amadeus_secret  # API secret (client secret)
        }

        # Send POST request to get access token
        response = requests.post(AUTH_URL, headers=headers, data=data)
        # Extract access token from response JSON
        self.token = response.json()["access_token"]

    def search_flights(self, original_location, destination_location, from_date, to_date):
        """
        Search for flight offers between origin and destination within given dates.

        Parameters:
        - original_location (str): IATA code of origin airport
        - destination_location (str): IATA code of destination airport
        - from_date (str): Departure date in 'YYYY-MM-DD' format
        - to_date (str): Return date in 'YYYY-MM-DD' format

        Returns:
        - List of flight offers (JSON data) from Amadeus API
        """
        headers = {
            "Authorization": f"Bearer {self.token}",  # Bearer token for authentication
            "Content-Type": "application/json"
        }
        body = {
            "originLocationCode": original_location,
            "destinationLocationCode": destination_location,
            "departureDate": from_date,
            "returnDate": to_date,
            "adults": 1,  # Number of adult passengers
            "nonStop": "true",  # Only non-stop flights
            "currencyCode": "INR",  # Currency code for price
            "max": "10",  # Max number of flight offers to return
        }

        # Send GET request with parameters to fetch flight offers
        response = requests.get(url=FLIGHT_OFFERS_URL, headers=headers, params=body)
        # Return the list of flight offers from the response JSON
        return response.json()["data"]

    def city_search(self, city):
        """
        Search for city and airport details within India by city name.

        Parameters:
        - city (str): Name or keyword of the city to search

        Returns:
        - JSON response containing city and airport information
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {
            "countryCode": "IN",  # Limit search to India
            "keyword": city,  # City keyword to search
            "max": 5,  # Maximum number of results
            "include": "AIRPORTS"  # Include airport information in response
        }
        # Send GET request to search for city and airport info
        response = requests.get(url=CITY_URL, headers=headers, params=body)
        return response.json()

    def find_cheapest_flight(self, date_range: list, origin_location_iata, destination_location_iata):
        """
        Find the cheapest flight within the specified date range for a round trip.

        Parameters:
        - date_range (list): List of datetime objects representing possible departure dates
        - origin_location_iata (str): IATA code of origin airport
        - destination_location_iata (str): IATA code of destination airport

        Returns:
        - Tuple containing:
          (lowest_price (float or "N/A"),
           outbound_date (str in 'YYYY-MM-DD' format or "N/A"),
           inbound_date (str in 'YYYY-MM-DD' format or "N/A"))
        """
        # Lists to hold prices and corresponding dates
        price_list = []
        outbound_date_list = []
        inbound_date_list = []

        # Iterate over each date in the date range to search flights
        for date in date_range:
            # Search flights with a 5-day round trip starting at 'date'
            flights = self.search_flights(
                original_location=origin_location_iata,
                destination_location=destination_location_iata,
                from_date=date.strftime("%Y-%m-%d"),
                to_date=(date + timedelta(days=5)).strftime("%Y-%m-%d")  # 5-day return trip
            )

            # Process each flight offer returned
            for flight in flights:
                # Extract the total price of the flight offer
                flight_price = float(flight["price"]["grandTotal"])
                # Extract outbound departure date-time string
                outbound_date = flight["itineraries"][0]["segments"][0]["departure"]["at"]
                # Extract inbound departure date-time string
                inbound_date = flight["itineraries"][1]["segments"][0]["departure"]["at"]

                # Append dates and price to respective lists
                outbound_date_list.append(outbound_date)
                inbound_date_list.append(inbound_date)
                price_list.append(flight_price)

        # If any flights were found, determine the cheapest one
        if price_list:  # Ensure list is not empty
            min_price = min(price_list)
            # Find the index of the cheapest flight
            min_index = price_list.index(min_price)
            # Extract corresponding outbound and inbound dates (date part only)
            return (
                min_price,
                outbound_date_list[min_index].split("T")[0],
                inbound_date_list[min_index].split("T")[0]
            )
        else:
            # Return "N/A" if no flights found
            return "N/A", "N/A", "N/A"

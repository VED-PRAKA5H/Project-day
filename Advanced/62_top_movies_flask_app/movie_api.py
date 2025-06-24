import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file located in the project directory
load_dotenv()

# Retrieve TMDB API key from environment variables
tmdb_api = os.getenv("TMDB_API")

# Base URL for TMDB's "Search Movie" API endpoint
base_url = "https://api.themoviedb.org/3/search/movie"

# HTTP headers to mimic a browser request and specify JSON as response format
headers = {
    "accept": "application/json",  # Expect JSON data in response
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.75 Safari/537.36'  # Browser-like User-Agent
}


def get_movies_list_tmdb(movie_name) -> list:
    """
    Search for movies on The Movie Database (TMDB) matching the given movie name.

    Args:
        movie_name (str): The search term for the movie title.

    Returns:
        list: A list of movie result dictionaries (can be empty if nothing found).
    """

    # Query parameters for the TMDB API request
    params = {
        "api_key": tmdb_api,  # Your TMDB API key from environment variables
        "query": movie_name  # The movie name to search for
    }

    try:
        # Make a GET request to TMDB API
        response = requests.get(base_url, headers=headers, params=params)

        # If request is successful (HTTP 200)
        if response.status_code == 200:
            # Parse JSON response into Python dictionary
            data = response.json()
            print(f"Successfully retrieved data for {params['query']}.")

            # Extract 'results' from JSON, return empty list if missing
            return data.get('results', [])

        else:
            # Print HTTP error code if the request was not successful
            print(f"Error for {params['query']}: Status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Catch any network or connection errors and print them
        print(f"An error occurred for {params['query']}: {e}")

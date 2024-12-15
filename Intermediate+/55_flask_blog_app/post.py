import requests


class Post:
    def __init__(self):
        """
        Initializes the Post object by fetching blog post data from a remote API.
        Stores the list of posts in self.posts.
        Includes error handling for network failures or invalid responses.
        """
        self.posts = []  # Default to empty list in case of error
        try:
            # Try to get JSON data from the provided URL
            response = requests.get("https://api.npoint.io/769bca525bc2f2bfe35b", timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

            # Try to decode JSON data
            data = response.json()
            if isinstance(data, list):
                self.posts = data
            else:
                print("Warning: The fetched data is not a list. Check your API response format.")
        except requests.exceptions.RequestException as e:
            print(f"Network/API error occurred while fetching posts: {e}")
        except ValueError as e:
            print(f"JSON decoding error: {e}")
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__}: {e}")

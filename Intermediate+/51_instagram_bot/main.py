import os
from dotenv import load_dotenv         # For loading environment variables from a .env file
from insta_follower import InstaFollower  # Import the InstaFollower class you defined earlier

load_dotenv()                          # Load variables from .env into the environment

URL = 'https://www.instagram.com/accounts/login/'  # Instagram login page URL

USERNAME = os.getenv("IG_USERNAME")    # Fetch Instagram username securely from environment variable
PASSWORD = os.getenv("IG_PASSWORD")    # Fetch Instagram password securely from environment variable
SIMILAR_ACCOUNT = 'cristiano'        # Target account for finding followers

# Initialize an InstaFollower object with the login URL
igf = InstaFollower(url=URL)

# Log in to Instagram using the credentials
igf.login(username=USERNAME, password=PASSWORD)

# Go to the target account and process its followers
igf.find_followers(account_user=SIMILAR_ACCOUNT)

# Quit the browser and clean up WebDriver session at the end of the script
igf.quit()


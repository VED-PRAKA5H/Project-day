from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from spotify_manager import SpotipyManager

# Load environment variables from .env file
load_dotenv()


def get_100_songs(search_date: str, region: str) -> list:
    """
    Returns a list of 100 (if available for india) song titles from Billboard for a particular date.
    Fetches either Indian or global charts based on the 'region' parameter.

    :param search_date: Date in YYYY-MM-DD format
    :param region: "I" for India, "W" for Worldwide
    :return: List of song titles (strings)
    """
    if region == "I":
        # Billboard URL for India charts
        billboard_url = f"https://www.billboard.com/charts/india-songs-hotw/{search_date}/"
    else:
        # Billboard URL for global Hot 100
        billboard_url = f"https://www.billboard.com/charts/hot-100/{search_date}/"

    headers = {
        "User-Agent": os.getenv("USER_AGENT")
    }

    # Send GET request to fetch chart page
    response = requests.get(url=billboard_url, headers=headers)
    contents = response.text

    # Parse page content with BeautifulSoup
    soup = BeautifulSoup(contents, "html.parser")
    # Find all list items containing song info
    music_details = soup.find_all(name="li", class_="lrv-u-width-100p")
    music_titles = []
    for music in music_details:
        # Extract the <h3> tag containing the song title
        h3_tag = music.find(name="h3", id="title-of-a-story")
        if h3_tag is not None:
            music_title = h3_tag.text.strip()
            music_titles.append(music_title)
    return music_titles


# Prompt the user for the desired date and region
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
zone = input("For Indian songs type I and for worldwide type W: ").upper()
while zone not in ("W", "I"):
    zone = input("Please enter a valid option:\nFor Indian songs type I and for worldwide type W: ").upper()

songs = get_100_songs(date, zone)

# Create a new Spotify playlist for the chosen Billboard chart
playlist_name = f"{zone}: {date} Billboard 100"
manager = SpotipyManager()
user_id = manager.get_current_user_id()
playlist_id = manager.create_playlist(playlist_name, user_id)

# Add each Billboard song to the playlist
for i, song in enumerate(songs):
    print(f"---------------------- Song: {i + 1} ----------------------")
    # Search for the track, optionally by year
    track_id = manager.search_track(track_name=song, year=date.split("-")[0], is_indian=zone)
    if track_id:
        result = manager.add_track_to_playlist(playlist_id, track_id)
    else:
        print("Track not found!")

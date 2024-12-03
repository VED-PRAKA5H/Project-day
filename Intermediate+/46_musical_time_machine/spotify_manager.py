from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)


load_dotenv()


class SpotipyManager:
    """
    Encapsulates Spotify API actions using Spotipy.
    Handles auth, user info, playlist creation, track search, and adding tracks to playlists.
    """

    # Define the necessary scopes as class-level constants
    PLAYLIST_MODIFY_PUBLIC_SCOPE = "playlist-modify-public"
    USER_LIBRARY_READ_SCOPE = "user-library-read"

    def __init__(self, scope=PLAYLIST_MODIFY_PUBLIC_SCOPE):
        """
        Initialize SpotipyManager with the provided scope(s).
        You can combine scopes as needed.
        """
        self.scope = scope
        self.sp = Spotify(auth_manager=SpotifyOAuth(scope=self.scope))

    def get_basic_user_info(self, user_name):
        """
        Fetch info for a given Spotify username.
        (Note: username is not always their display name!)
        """
        logging.info("Found user information.")
        return self.sp.user(user_name)

    def get_current_user_id(self):
        """
        Get the authorized user's ID.
        """
        logging.info("Found user id")
        return self.sp.current_user()['id']

    def create_playlist(self, playlist_name, user_id):
        """
        Create a new public playlist for the user.
        Returns the new playlist's ID.
        """
        playlist = self.sp.user_playlist_create(user=user_id, name=playlist_name)
        logging.info(f"Created playlist {playlist['id']}")
        return playlist['id']

    def get_current_playlist_id(self):
        """
        Returns the ID of the first playlist in the current user's playlists,
        or None if no playlists exist.
        """
        playlists = self.sp.current_user_playlists(limit=1)
        items = playlists['items']
        if not items:
            logging.info("No playlists found for the user.")
            return None
        logging.info("Found playlist: %s", items[0]['name'])
        return items[0]['id']

    def search_track(self, track_name, year: str, is_indian):
        """
        Search for the first matching track by track name.
        if is indian  = "I" then search in india
        Returns the track's Spotify ID, or None if not found.
        """

        if is_indian == "I":
            query = f"track:{track_name}"
            results = self.sp.search(q=query, type="track", limit=1, market="IN")
        else:
            query = f"track:{track_name} year:{year}"
            results = self.sp.search(q=query, type="track", limit=1)
        items = results['tracks']['items']
        if not items:
            return None
        logging.info(f"Found the Track {items[0]['id']}")
        return items[0]['id']

    def add_track_to_playlist(self, playlist_id, track_id):
        """
        Add the given track to the playlist.
        Returns the API response.
        """
        result = self.sp.playlist_add_items(playlist_id=playlist_id, items=[track_id])
        logging.info("Added the song in the playlist")
        return result

# 🎼 Musical Time Machine
**Create Spotify playlists for any date in the past using Billboard’s charts!**
This tool scrapes song data from Billboard (India or Worldwide) for a selected date, then creates a corresponding Spotify playlist with those songs—automatically.

## 🔧 Prerequisites

- **Spotify Account**  
  If you don’t have one, [sign up here](https://www.spotify.com/signup/).

- **Spotify Developer Application**
  1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
  2. Create a new app.
  3. Copy your **Client ID** and **Client Secret**.
  4. Set a Redirect URI (for local development, e.g. `http://127.0.0.1:8000/callback`).

- **Python Libraries**
  - [Spotipy](https://spotipy.readthedocs.io/) (for Spotify API):  
    `pip install spotipy`
  - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (for web scraping):  
    `pip install beautifulsoup4`
  - [python-dotenv](https://pypi.org/project/python-dotenv/) (for `.env` support):  
    `pip install python-dotenv`
  - [requests](https://pypi.org/project/requests/) (for HTTP requests):  
    `pip install requests`

- **Billboard**  
  No package required; data is scraped from [billboard.com](https://www.billboard.com/).

- **Create a `.env` file** in the root directory and add your Spotify credentials:
    ```env
    SPOTIPY_CLIENT_ID=your-spotify-client-id
    SPOTIPY_CLIENT_SECRET=your-spotify-client-secret
    SPOTIPY_REDIRECT_URI=http://127.0.0.1:8000/callback
    USER_AGENT=your-user-agent-string     
    ```

    *(For USER_AGENT, copy your browser’s user agent string. It may help if requests to Billboard fail.) [From here](https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/)*

## 🚀 How to Use

1. **Run the main program:**
    ```bash
    python main.py
    ```
2. **Follow the prompts:**
    - Enter a date (`YYYY-MM-DD`)
    - Choose `I` for India or `W` for Worldwide charts

3. **The program will:**
    - Scrape Billboard’s top 100 songs for the date/region you selected
    - Create a new Spotify playlist with those songs in your account

## 📝 Notes

- **Authentication:**  
  On your first run, Spotipy will open a browser for you to log in and authorize access.
- **Make sure your `.cache` (Spotipy token cache) is in your `.gitignore`:**

    ```
    .cache*
    ```
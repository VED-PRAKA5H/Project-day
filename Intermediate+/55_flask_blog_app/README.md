# Flask Blog App

A clean, dynamic blogging application built with **Flask**. It fetches blog posts from a remote API, displays them on a beautiful index page, and renders individual posts with an aesthetic design. The site uses robust error handling and modern HTML/CSS for an engaging, responsive experience.

## Features

- Lists blog posts fetched from a JSON API.
- Individual post pages with elegant design.
- Current year and author in the footer, updated automatically.
- Robust error handling for networking, API, and invalid routes.
- Clean structure with separation of logic (`main.py`), data (`post.py`), templates, and static assets.

## Project Structure

```text
your-project/
│
├── main.py             # Flask application (entry point)
├── post.py             # Post class to fetch and parse API data
├── templates/
│   ├── index.html      # Homepage/blog index template
│   └── post.html       # Single post detail template
│
├── static/
│   └── css/
│        ├── index.css  # Main CSS for blog index
│        └── post.css   # CSS for single post pages
│
└── README.md           # This file
```

## Prerequisites

- **Python 3.7+**
- **Flask** (`pip install Flask`)
- **requests** (`pip install requests`)

## Setup & Usage

1. **Install dependencies:**
    ```bash
    pip install Flask requests
    ```

2. **Update the API URL:**  
   In `post.py`, set your API endpoint to a valid URL (replace the `xxxxxxxxxxxxb` with your own API id/key).

3. **Run the app:**
    ```bash
    python main.py
    ```

4. **Visit in browser:**  
   Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the blog index page.
   - Click "Read" on any post to view its full content.

## Customization

- **Templates:**  
  You can easily style or expand templates in the `templates/` folder. Separate index/blog and post display for flexibility.
- **CSS Styles:**  
  All main CSS is under `static/css/`. Edit `index.css` or `post.css` for global or page-specific styles. Google Fonts are integrated for a clean look.
- **Post data:**  
  Blog post data comes from your API in `post.py` (expects an array of posts with `id`, `title`, `subtitle`, `body` fields).

## Error Handling

If the API is unreachable or returns invalid data, users see a console warning and the blog will display as empty.


## Example post.py

```python
import requests

class Post:
    def __init__(self):
        self.posts = []  # Empty by default
        try:
            response = requests.get("https://api.npoint.io/xxxxxxxxxxxxb", timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                self.posts = data
            else:
                print("API response is not a list.")
        except requests.exceptions.RequestException as e:
            print(f"API network error: {e}")
        except ValueError as e:
            print(f"Error parsing JSON: {e}")
```

(See the provided `main.py` for the full app logic and error handling.)



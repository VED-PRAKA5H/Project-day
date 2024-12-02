# Movies Scraper

A Python script that scrapes the list of the 100 Greatest Movies from the archived Empire Online web page using `requests` and `BeautifulSoup`. 
The script extracts movie titles and saves them into a text file.

***

### Features
- Fetches the HTML content from the archived Empire Online page listing the 100 Greatest Movies.  
- Parses the page using BeautifulSoup to extract movie titles.  
- Saves the extracted movie titles in reverse order (oldest first) to a local `movies.txt` file.  
- Handles text encoding for safe file writing.

***

### Requirements
- Python 3.x  
- `requests` library to fetch web content.  
- `beautifulsoup4` library to parse and extract HTML elements.

Install dependencies via pip:

```bash
pip install requests beautifulsoup4
```

***

### How to Run

1. Run the script:

    ```bash
    python main.py
    ```

2. The script will download the web page, parse out the movie titles, and save them in `movies.txt` in the same directory.  
3. Open `movies.txt` to see the full list of movie titles.

***

### Code Overview

- Sends HTTP GET request to `https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/`.  
- Parses the HTML response and finds all `<h3>` tags with class attribute `"title"`.  
- Extracts the text content of each title and reverses the order to list oldest first.  
- Writes the titles line-by-line into `movies.txt` with UTF-8 encoding.

***

### References

- [Requests documentation](https://docs.python-requests.org/en/latest/)  
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [Empire Online - 100 Greatest Movies (Archived)](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/)

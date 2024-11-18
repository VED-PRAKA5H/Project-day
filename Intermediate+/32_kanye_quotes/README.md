# Kanye Quotes

A simple Python Tkinter GUI app that fetches and displays random Kanye West quotes using the public API [https://api.kanye.rest/](https://api.kanye.rest/).

***

### Features
- Fetches a random Kanye quote on button click via API request.  
- Dynamically adjusts font size to fit quote length.  
- Clean, minimalistic interface with a Kanye-themed background and button image.  
- Uses Python's `requests` library to interact with the RESTful API.  
- Lightweight and easy to run with minimal dependencies.

***

### Requirements
- Python 3.x  
- `requests` library:

```bash
pip install requests
```

- Image files in the project folder:
  - `background.png` (background image for canvas)  
  - `kanye.png` (button image for quote fetching)  

***

### How to Run

Run the main script:

```bash
python main.py
```

Click the Kanye image button to fetch a new random quote from the API and display it on the canvas.

***

### Code Overview

- `get_quote()` function makes a GET request to Kanye REST API, parses the JSON response to extract the quote, and updates the canvas text widget.  
- Dynamically adjusts font size so longer quotes fit nicely within the canvas.  
- Tkinter canvas is used to show background image and quote text layered on top.  
- Image button triggers fetching a new quote on click.

***

### References

- [Kanye REST API](https://api.kanye.rest/)  
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [Requests Library](https://requests.readthedocs.io/en/latest/)  

# Flask Guess the Number App

A simple and fun number guessing web application built with Flask. 
The app picks a random number between 0 and 9 on server start and lets users guess the number by entering their guess as a URL path parameter. 
It gives immediate feedback on whether the guess is too high, too low, or correct - all responses are beautifully and consistently centered with embedded GIFs to enhance user experience.

## Features

- Random number generated at server launch, stays unchanged until restart.
- Users submit guesses by adding the number at the end of the URL (e.g., `/5`).
- Immediate feedback messages for guesses: "Too high", "Too low", or "You are right".
- All responses are styled and center-aligned via a custom Flask decorator.
- Fun GIFs add visual interest and clarity to responses.
- Clean, minimal, and extensible codebase.

## Project Structure

```text
project/
│
├── server.py              # Main Flask application file (entry point)
└── README.md           # This readme file
```

## Prerequisites

- Python 3.7+
- Flask (install with `pip install Flask`)

## Setup & Usage

### Install dependencies

```bash
pip install Flask
```

### Run the app

```bash
python server.py
```

### Access the app

Open your browser and visit:

```
http://127.0.0.1:5000/
```

- This shows instructions on how to play.
- To make a guess, enter your number (0-9) as a URL path, e.g., `http://127.0.0.1:5000/4`

### Example guesses

- `http://127.0.0.1:5000/7` — Flask responds with "Too high" or "Too low" or "You are right".

## Customization

- **Change the number range:** Modify the `randint(0, 9)` call in `app.py` to change the guessing range.
- **Update styling:** Modify or extend the `center_div` decorator to add more CSS styles or HTML wrappers.
- **Add templates:** Move inline HTML to template files for easier maintenance and advanced layouts.
- **Enhance game logic:** Add features like multiple attempts, score tracking, or a reset mechanism.

# Cafe & WiFi Ratings Flask App

A Flask web application for collecting and displaying information about local cafes—including their location, opening hours, and ratings for coffee, WiFi, and power outlets. Uses **Flask-WTF** forms, **Flask-Bootstrap5**, and stores data in a CSV file.

***

### Features

- **Add Cafes:** Fill and submit a form with cafe details, including Google Maps link and ratings.
- **View Cafes:** Browse all submitted cafes in a formatted table.
- **Form Validation:** Utilizes Flask-WTF and WTForms validators for clean input.
- **Intuitive Ratings:** Use emojis to rate coffee, Wi-Fi quality, and power outlet availability.

***

### Project Structure

```
project/
├── main.py                # Main application file
├── cafe-data.csv         # Collected cafe data (auto-generated)
├── templates/            # HTML templates
│   ├── index.html
│   ├── add.html
│   ├── cafes.html
│   └── success.html
└── requirements.txt      # List of dependencies
```

***

### Installation

1. Clone the repository:

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

***

### Usage

1. Start the development server:
    ```bash
    python app.py
    ```

2. Open in a browser:
    ```
    http://127.0.0.1:5000/
    ```

3. To add a cafe, go to `/add`:
    ```
    http://127.0.0.1:5000/add
    ```

4. To view all cafes, go to `/cafes`:
    ```
    http://127.0.0.1:5000/cafes
    ```

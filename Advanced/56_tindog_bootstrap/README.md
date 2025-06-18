# TinDog – Bootstrap Demo App

A responsive single-page website project built with Bootstrap, themed as a dating platform for dogs ("TinDog"). Showcases Bootstrap layout, navigation, grid, cards, and responsive design.

***

## Prerequisites

- Modern web browser (Chrome, Firefox, Edge, etc.)
- Optional: Local web server (e.g. Python’s `http.server`) for some browser security restrictions on loading local assets

***

## Project Structure

```text
project/
│
├── css/
│   └── style.css        # Custom styles
│
├── images/              # All images used in the site
│   ├── iphone.png
│   ├── dog-img.jpg
│   ├── mashable.png
│   ├── techcrunch.png
│   ├── tnw.png
│   └── bizinsider.png
│
├── index.html           # Main HTML file
│
└── README.md            # This file
```

***

## Setup & Run

1. **Clone or download** the project folder to your computer.

2. Ensure the directory structure matches the one above – keep `index.html` in the root, with `css/` and `images/` folders beside it, containing the included assets.

3. *(Optional but recommended)* If you want to avoid CORS or local file security warnings, start a simple local server. For example, with Python 3:

    ```bash
    python -m http.server
    ```

    Then open [http://localhost:8000](http://localhost:8000) in your browser.

4. Otherwise, you can simply **double-click `index.html` to open it** in your browser.

***

## Features

- Responsive design using [Bootstrap 5](https://getbootstrap.com/)
- Custom sections: hero, features, testimonials, pricing, and footer
- SVG icons and logo
- Sample images and test data structure (replace images/text as needed)

***

## Customization

- **Edit styles**: Change styles in `css/style.css`
- **Replace images**: Swap out files in `images/` for your own branding/content
- **Add pages/features**: Extend functionality by adding new Bootstrap components as needed

***

## Credits

- Bootstrap 5 CDN
- Icons from Bootstrap Icons
- Demo images (placeholders; replace with your own content as needed)

***

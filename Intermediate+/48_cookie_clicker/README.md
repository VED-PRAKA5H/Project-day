# Cookie Clicker Auto Buyer Bot
Automate gameplay of the [Cookie Clicker](https://ozh.github.io/cookieclicker/) web game by automatically clicking the cookie and purchasing upgrades using Selenium WebDriver.

## 🔧 Prerequisites
- **Python 3.x** — Code is written in Python
- **Selenium** — For browser automation  
  Install with:  
  ```bash
  pip install selenium
  ```
- **ChromeDriver** — Required for controlling Chrome browser; ensure it matches your Chrome browser version  
  Download from [ChromeDriver official site](https://sites.google.com/chromium.org/driver/)
- **Google Chrome** — The browser to automate

## ✨ Features
- Automatically clicks the big cookie repeatedly to generate cookies
- Periodically checks available upgrades/shop items and upgrades when affordable
- Handles dynamic page changes gracefully by catching exceptions like stale element references
- Keeps Chrome browser open after script ends for inspection/debugging
- Runs continuously until a predefined duration (5 minutes) is reached, then outputs the final cookie generation rate

## 🚀 How It Works (Overview)
- Initializes Selenium Chrome WebDriver with options to keep browser open on exit
- Navigates to the Cookie Clicker game URL and selects language
- In a loop:
  - Clicks the big cookie to generate cookies
  - Every 5 seconds, fetches store item prices and current cookies count
  - Buys the most expensive upgrade affordable based on available cookies
  - Handles frequent DOM updates and exceptions by retrying as needed
- Stops after 5 minutes and prints cookies/sec performance

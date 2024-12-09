# Automating Data Entry with Web Scraping
Automates the process of collecting rental listings from Zillow and submits them into a Google Form for structured storage.

## Prerequisites
- **Python Packages:** `pip install bs4 selenium python-dotenv`
- **ChromeDriver:** Download and add [ChromeDriver](https://chromedriver.chromium.org/) to your system PATH (ensure it matches your Chrome browser version).

## Setup & Usage
1. **Configure Google Form:**  
   - Create a Google Form with fields for Address, Price, and Property URL.
   - Add the form link to a `.env` file as `GFORM_LINK=your_google_form_url`.
2. **Update Script:**  
   - The script scrapes all San Francisco rentals on Zillow priced up to $3,000/month with 1+ bedrooms.
   - It collects price, address, and listing URL using BeautifulSoup.
3. **Run the Script:**  
   - The script will automatically fill and submit the Google Form for each rental using Selenium.
4. **View Results:**  
   - Access the responses in Google Sheets from the form's Responses tab, containing all scraped data.


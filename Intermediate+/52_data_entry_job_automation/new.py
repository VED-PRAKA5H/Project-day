# THIS PROJECT IS ON THE LIVE WEBSITE OF ZILLOW

import os  # For loading environment variables
import random  # To introduce delays that mimic human actions
import time  # For sleep operations
from dotenv import load_dotenv  # To securely load secrets
from bs4 import BeautifulSoup  # For parsing HTML content
from selenium import webdriver  # For controlling browser actions
from selenium.webdriver.common.by import By  # For element selection strategies in Selenium
from selenium.webdriver.common.keys import Keys  # For simulating keyboard keys
import requests  # To fetch web pages directly

load_dotenv()  # Load environment variables from .env file

GFORM_URL = os.getenv("GFORM_LINK")  # Google Form link (from .env)
# Zillow rentals URL (pointing to San Francisco with filters in place)
ZILLOW_URL = ('https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C'
              '%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.53993121508789%2C%22east%22%3A-122'
              '.27282611254883%2C%22south%22%3A37.70017963709451%2C%22north%22%3A37.8638001429755%7D%2C'
              '%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22'
              '%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B'
              '%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D'
              '%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B'
              '%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A594032%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C'
              '%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%7D')

# Browser-like headers help bypass some basic anti-bot detection mechanisms on Zillow
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "Referer": "https://www.zillow.com/",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": 'Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

# Request the Zillow search result page using the headers above
response = requests.get(url=ZILLOW_URL, headers=headers)
contents = response.text  # Raw HTML content

if response.status_code == 200:
    print("Got the data. Status code: ", response.status_code)
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(markup=contents, features='html.parser')
    renting_grid = soup.find(id="grid-search-results")  # The main block with property listings
    renting_list = renting_grid.find_all("li")  # Each <li> is a property

    locations = []
    prices = []
    links = []
    for room in renting_list:
        a_tag = room.findNext("a")  # Link tag for details page
        links.append(a_tag.get('href').strip())

        # Try to extract address; if <address> tag fails, fallback to anchor text
        try:
            address = a_tag.findNext('address').text.strip()
        except Exception as e:
            address = a_tag.text.strip()
        locations.append(address)

        # Try to extract the price; account for variations by tag/class
        try:
            price = room.findNext(name='span', class_='jCoXOF')
        except Exception as e:
            price = room.find(name='span', class_='jCoXOF')
        if price is not None:
            if '+' in price.text.strip():
                prices.append(price.text.strip().split("+")[0])  # Get price before plus sign
            else:
                prices.append(price.text.strip().split("/")[0])  # Get price before per month, etc.
        else:
            prices.append("N/A")  # No price found, placeholder

    print(f"Scraped the details of {len(renting_list)} rooms.\nOpening the google form via Selenium.")
    # Set up Selenium Chrome browser (headless option can be added if no GUI is needed)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)  # Keeps browser open after script ends
    driver = webdriver.Chrome(options=chrome_options)
    print("Opened the Google form")

    for link, price, location in zip(links, prices, locations):
        driver.get(url=GFORM_URL)  # Open Google Form for every room
        time.sleep(random.randint(4, 7))  # Human-like delay between submissions
        if price == "N/A":
            print("Scraped page 1")
            break
        else:
            try:
                # Try to find address field by XPath and submit details using TAB/ENTER
                address_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
                )
                address_element.send_keys(location, Keys.TAB, price, Keys.TAB, link, Keys.TAB, Keys.ENTER)
            except Exception as e:
                # Fallback: Use CSS selector if XPath fails
                address_element = driver.find_element(by=By.CSS_SELECTOR, value='.whsOnd.zHQkBf')
                address_element.send_keys(location, Keys.TAB, price, Keys.TAB, link, Keys.TAB, Keys.ENTER)

            print("Filled: ", link, price, location)
    print("Form have been filled with rooms specifications.\nTASK COMPLETED!")
    driver.quit()  # Always close/quit browser session
else:
    print(f"Didn't get the response from https://www.zillow.com/. Status: {response.status_code}")  # Error handling

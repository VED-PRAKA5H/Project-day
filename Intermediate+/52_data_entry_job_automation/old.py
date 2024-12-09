# THIS PROJECT IS ON THE CLONE WEBSITE OF ZILLOW

import os
import random
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

# Load environment variables from a .env file for securely sourcing sensitive data like URLs
load_dotenv()

# Fetch the Google Form URL from environment variable
GFORM_URL = os.getenv("GFORM_LINK")

# Make an HTTP request to the sample Zillow-Clone website to scrape property data
response = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')
contents = response.text

if response.status_code == 200:
    print("Got the data", response.status_code)

    # Parse the HTML content using BeautifulSoup for data extraction
    soup = BeautifulSoup(markup=contents, features='html.parser')

    # Find all property listings by their specific CSS class
    renting_list = soup.find_all(class_='ListItem-c11n-8-84-3-StyledListCardWrapper')
    locations = []
    prices = []
    links = []

    # Extract data for the last three properties only
    for room in renting_list[-3:]:
        # Extract and clean the property link
        links.append(room.findNext('a').get('href').strip())
        # Extract and clean the address/location information
        locations.append(room.find("a").getText().strip())
        # Extract and clean the price (remove anything after "/" and strip '+')
        prices.append(room.findNext(name='div', class_='PropertyCardWrapper').getText().strip().split("/")[0].replace('+', ''))

    print("Scraped the details.\nOpening the google form via Selenium.")

    # Set up Selenium for automating browser actions
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)  # Keeps browser window open after script finishes
    driver = webdriver.Chrome(options=chrome_options)
    print("Opened the Google form")

    # Loop through the scraped data and submit each property to the Google Form
    for link, price, location in zip(links, prices, locations):
        driver.get(url=GFORM_URL)
        # Randomized sleep to mimic human interaction and avoid detection as a bot
        time.sleep(random.randint(1, 3))
        try:
            # Locate address input field by XPath and fill all required data using TABs to move to next input
            address_element = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_element.send_keys(location, Keys.TAB, price, Keys.TAB, link, Keys.TAB, Keys.ENTER)
        except Exception as e:
            # Backup: Try finding the form fields by their CSS selector if XPath fails (for robustness)
            address_element = driver.find_element(by=By.CSS_SELECTOR, value='.whsOnd.zHQkBf')
            address_element.send_keys(location, Keys.TAB, price, Keys.TAB, link, Keys.TAB, Keys.ENTER)

        print("Filled: ", link, price, location)
    print("Form have been filled with rooms specifications.\nTASK COMPLETED!")
    driver.quit()
else:
    # Print the error if unable to fetch data from the site
    print(f"Didn't get the response from https://www.zillow.com/. Status: {response.status_code}")

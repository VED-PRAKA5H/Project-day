from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure Chrome to stay open even after the script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the Cookie Clicker game webpage
driver.get(url="https://ozh.github.io/cookieclicker/")

# Implicitly wait up to 10 seconds for elements to appear if not immediately present
driver.implicitly_wait(10)

start = time.time()
initial_time = start
print("Looking for language selection...")
# Select the default language (clicks the language selection button)
lang = driver.find_element(by=By.CLASS_NAME, value="langSelectButton")
lang.click()
print("Found language button, clicking...")
while True:
    product_price = []
    try:
        # Main game loop: try to find & click the main cookie
        cookie = driver.find_element(by=By.ID, value='bigCookie')
        cookie.click()

        # Every 5 seconds, attempt to check/upgrade store items
        if time.time() - start >= 10:
            start = time.time()
            # Get all elements displaying store item prices
            store = driver.find_elements(by=By.CLASS_NAME, value='price')

            # If any store upgrades or products are available
            if len(store) > 0:
                for product in store:
                    # Only consider valid price entries (some may be blank if locked)
                    if product.text.strip() != "":
                        # Convert price from string to integer (strip commas)
                        product_price.append(int(product.text.strip().replace(",", "")))

                # Find total cookies owned. Extract just number before first space.
                cookies = driver.find_element(by=By.ID, value="cookies")
                cookies_no = int(cookies.text.split(" ")[0].replace(",", ""))

                # Stop after 5 minutes (5*60 seconds)
                if time.time() - initial_time >= 8*60:
                    print("Cookies/second: ", cookies.text.split(" ")[-1])
                    break

                # Try to buy the most expensive affordable upgrade (highest price first)
                for price in reversed(product_price):
                    if cookies_no >= price:
                        try:
                            # Get index in product_price to target the correct product element
                            index = product_price.index(price)
                            # Find the corresponding store product element and click to buy
                            item = driver.find_element(by=By.ID, value=f"product{index}")
                            item.click()
                            print(f"Bought item: product{index}")
                        except Exception as e:
                            # Ignore click errors (may be stale/blocked/unavailable)
                            print(f"Couldn't find product. Now clicking...")
                            continue

    except Exception as e:
        # General catch-all: skip this iteration for any unexpected errors
        print(f"Couldn't find the store. Now clicking...")
        continue

# Clean up: close the browser window (note: detach=True means it might stay open)
driver.quit()

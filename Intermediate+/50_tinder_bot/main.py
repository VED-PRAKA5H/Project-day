import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv

# Load environment variables (.env) for credentials
load_dotenv()  # Loads FACEBOOK_EMAIL and FACEBOOK_PASSWORD

fb_email = os.getenv("FACEBOOK_EMAIL")  # Facebook email from environment
fb_password = os.getenv("FACEBOOK_PASSWORD")  # Facebook password from environment

# Chrome setup with option to keep browser open after script
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Detach: keeps browser open

driver = webdriver.Chrome(options=chrome_options)  # Initialize Chrome driver

URL = "https://tinder.com/"  # Tinder main page URL
driver.get(url=URL)  # Launch Tinder

base_window = driver.window_handles[0]  # Store the main window handle

# Wait for main page to load
time.sleep(7)  # Can be optimized with WebDriverWait

print("Trying to log in...")
login_btn = driver.find_element(By.XPATH, '//*[@id="q1144275170"]/div/div[1]/div/main/div[1]/div/div/div/div/div['
                                          '1]/header/div/div[2]/div[2]')  # Find login button
try:
    login_btn.click()  # Attempt click
except Exception:
    login_btn.send_keys(Keys.ENTER)  # Fallback if click doesn't work

print("Clicked log in button")

wait = WebDriverWait(driver, 10)  # Prepare a Wait object

# Attempt to find and click the Facebook login button
try:
    fb_btn = driver.find_element(By.XPATH,
                                 '//*[@id="q-584105906"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button')  # Facebook login button
    fb_btn.click()
except Exception:
    time.sleep(7)  # Wait before another attempt
    try:
        fb_btn = driver.find_element(By.XPATH, '//*[@id="q-584105906"]/div/div[1]/div/div[2]/div/div/div[2]/div['
                                               '2]/span/div[2]/button')
        fb_btn.click()
        print("Clicked Facebook login page button")
    except Exception:
        print("Didn't find Facebook login -- trying 'More Options'")
        more_options_btn = driver.find_element(By.XPATH,
                                               '//*[@id="q-584105906"]/div/div[2]/div/div/div[1]/div[1]/button')
        more_options_btn.click()
        print("Clicked 'More Options'")
        alt_fb_btn = driver.find_element(By.XPATH,
                                         '//*[@id="q-584105906"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/button')
        alt_fb_btn.click()
        fb_btn = driver.find_element(By.XPATH, '//*[@id="q-584105906"]/div/div[1]/div/div[2]/div/div/div[2]/div['
                                               '2]/span/div[2]/button')
        fb_btn.click()
        print("Opened Facebook login page")

time.sleep(2)  # Wait for FB window to spawn

all_windows = driver.window_handles  # Capture all open window handles
fb_login_window = all_windows[1]  # Second handle is Facebook popup
driver.switch_to.window(fb_login_window)  # Switch Selenium to FB window

print(driver.title)  # Should print "Facebook" if we're on FB

# Enter FB credentials and log in
try:
    email_box = driver.find_element(By.ID, "email")  # Find email field
    email_box.send_keys(fb_email)  # Enter email
    password_box = driver.find_element(By.NAME, "pass")  # Find password field
    password_box.send_keys(fb_password)  # Enter password
    driver.find_element(By.NAME, "login").click()  # Click login
    # Optional: Dismiss additional dialogs/popups if needed
    print("Successfully Logged in on Facebook!")
except Exception as e:
    print("Failed Facebook login:", e)

driver.switch_to.window(base_window)  # Switch back to Tinder

# Tinder Like automation (free: 100/day)
for n in range(100):  # 100 likes loop
    time.sleep(1)  # Delay between likes
    try:
        like_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div['
                                                 '1]/div/div[2]/div[4]/button')  # Like button
        like_btn.click()  # Attempt like
    except ElementClickInterceptedException:  # Popup in front of like
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")  # Find Match popup
            match_popup.click()  # Dismiss popup
        except NoSuchElementException:
            time.sleep(2)  # Wait if neither element is present

driver.quit()  # Close the browser at the end

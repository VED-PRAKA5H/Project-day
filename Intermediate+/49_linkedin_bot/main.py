import os
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
linkedin_phone = os.getenv("LINKEDIN_PHONE")

# Set up Chrome options (keeps browser open after script ends)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# LinkedIn Jobs search URL
URL = (
    "https://www.linkedin.com/jobs/search/?currentJobId=4277153596&f_AL=true&f_E=1%2C2&f_WT=2&geoId=92000000&"
    "keywords=data%20entry&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
)
driver.get(URL)

wait = WebDriverWait(driver, 15)

# Helper function to find clickable login button via multiple selectors
def find_login_button():
    selectors = [
        (By.CLASS_NAME, "sign-in-modal__outlet-btn"),
        (By.XPATH, '/html/body/div[5]/div/div/section/div/div/div/div[2]/button'),
        (
            By.XPATH,
            '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button',
        ),
    ]
    for by, value in selectors:
        try:
            return wait.until(EC.element_to_be_clickable((by, value)))
        except Exception:
            continue
    raise Exception("Login button not found!")

# Click login button (try click, fallback to sending ENTER key)
login_button = find_login_button()
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
try:
    login_button.click()
except Exception:
    login_button.send_keys(Keys.ENTER)

# Find email input box (try by NAME then by XPATH)
try:
    email_box = wait.until(EC.presence_of_element_located((By.NAME, "session-key")))
except Exception:
    email_box = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
        )
    )

print("Trying to login")
# Enter login credentials
email_box.send_keys(linkedin_email, Keys.TAB, linkedin_password, Keys.TAB * 3 + Keys.ENTER)

print("Successfully logged in!")

# Helper function to abort complex application by clicking Close and Discard
def abort_application():
    try:
        close_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-modal__dismiss"))
        )
        close_button.click()
        time.sleep(1)  # small delay for modal animation
        discard_buttons = driver.find_elements(
            By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"
        )
        if len(discard_buttons) > 1:
            discard_buttons[1].click()
        else:
            print("Discard button not found in modal.")
        time.sleep(1)
    except Exception as e:
        print(f"Error while aborting application: {e}")

# Wait a moment for listings to load
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

print(f"Found {len(all_listings)} job listings.")

for idx, listing in enumerate(all_listings, 1):
    print(f"\nOpening listing {idx}/{len(all_listings)}")
    try:
        listing.click()
    except Exception:
        print("Failed to click listing, skipping.")
        continue

    # Wait for the apply button to appear
    try:
        apply_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-s-apply button"))
        )
        apply_button.click()
    except Exception:
        print("No apply button found, skipping listing.")
        continue

    time.sleep(3)  # wait for application modal to load

    try:
        # Fill phone number if input is empty
        phone_input = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if not phone_input.get_attribute("value").strip():
            phone_input.send_keys(linkedin_phone)
    except NoSuchElementException:
        print("Phone input not found, continuing without filling phone.")

    # Locate the submit button at the modal footer
    try:
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        data_control_name = submit_button.get_attribute("data-control-name")

        if data_control_name == "continue_unify":
            abort_application()
            print("Complex application detected, skipped.")
            continue

        print("Submitting job application")
        submit_button.click()
    except NoSuchElementException:
        abort_application()
        print("Submit button not found, skipped.")
        continue

    time.sleep(2)  # wait for submission response

    # Close the application modal
    try:
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("Close button not found after submitting.")

    time.sleep(2)  # stable pause before next listing

print("Finished processing all job listings.")

# driver.quit()

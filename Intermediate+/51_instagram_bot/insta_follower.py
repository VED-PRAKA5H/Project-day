from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.window import WindowTypes
import time
import random
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def human_typing(element, text):
    """
    Type text into a web element simulating human keystrokes by introducing
    random delays between each character.

    Args:
        element: Selenium WebElement to send keys to.
        text: String text to type.
    """
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.4))  # Random delay to simulate natural typing speed


class InstaFollower:
    def __init__(self, url):
        """
        Initialize the Chrome webdriver with stealth options and open the given URL.

        Args:
            url: URL string to open (Instagram login page).
        """
        # Step 1: Chrome options to help evade Selenium detection
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")  # Maximize window for realism

        # Set realistic user-agent: customize if you want
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )

        # Disable blink features to reduce detection
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # Remove Selenium automation flags and extensions
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # Keep the browser window open after script finishes (useful while debugging)
        chrome_options.add_experimental_option("detach", True)

        # Initialize the Chrome driver with options
        self.driver = webdriver.Chrome(options=chrome_options)

        # Step 2: Random wait before starting interactions to mimic human behavior
        time.sleep(random.uniform(1, 5))

        # Open the login URL
        self.driver.get(url)
        logging.info(f"Opened the URL: {url}")

    def wait_for_element(self, by, value, timeout=20):
        """
        Reusable explicit wait function for waiting until element is present on the page.

        Args:
            by: Locator type (from selenium.webdriver.common.by.By).
            value: Locator string (e.g., 'username' or XPath).
            timeout: Max wait time in seconds.

        Returns:
            Selenium WebElement once found.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            logging.error(f"Element located by {by}='{value}' not found within {timeout} seconds.")
            raise e

    def human_mouse_movement(self, x_offset=100, y_offset=100):
        """
        Simulates human mouse movement by moving the cursor by given pixel offsets.

        Args:
            x_offset: Horizontal pixels to move.
            y_offset: Vertical pixels to move.
        """
        action = ActionChains(self.driver)
        action.move_by_offset(x_offset, y_offset).perform()
        logging.debug(f"Moved mouse by offset x: {x_offset}, y: {y_offset}")

    def human_scroll(self, to=None):
        """
        Simulate human-like scrolling randomly to top or bottom of the page,
        or to a specified position.

        Args:
            to: 'top', 'bottom', or None to randomly choose.
        """
        if to is None:
            to = random.choice(['top', 'bottom'])

        if to == 'bottom':
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            logging.debug("Scrolled to bottom of the page")
        elif to == 'top':
            self.driver.execute_script("window.scrollTo(0, 0);")
            logging.debug("Scrolled to top of the page")

        # Small pause after scrolling to allow page to settle
        time.sleep(random.uniform(1, 2))

    def login(self, username, password):
        """
        Automate Instagram login by typing username and password with human-like behavior
        and clicking login button.

        Args:
            username: Instagram username string.
            password: Instagram password string.
        """
        logging.info("Starting login process...")
        # Wait for username field to be present and type username
        user_element = self.wait_for_element(By.NAME, "username")
        human_typing(user_element, username)
        logging.info("Entered username")

        # Simulate mouse movement and scrolling before entering password
        self.human_mouse_movement()
        self.human_scroll()

        # Wait for password field and type password
        password_element = self.wait_for_element(By.NAME, "password")
        human_typing(password_element, password)
        logging.info("Entered password")

        # Find and click the login button
        login_button = self.wait_for_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        logging.info("Clicked login button, login submitted")

        # Wait for some seconds to allow login to process
        time.sleep(random.uniform(5, 7))

    def find_followers(self, account_user):
        """
        Open a new tab, navigate to the specified user's Instagram profile,
        click to view their followers, and scroll through the followers list.

        Args:
            account_user: Instagram username of the account to fetch followers from.
        """
        logging.info(f"Fetching followers for user: {account_user}")

        # Print and switch to a new browser tab
        original_tab = self.driver.current_window_handle
        self.driver.switch_to.new_window(WindowTypes.TAB)
        logging.info(f"Switched from original tab ({original_tab}) to new tab")

        # Navigate to the target user's Instagram profile
        profile_url = f"https://www.instagram.com/{account_user}/"
        self.driver.get(profile_url)
        logging.info(f"Opened profile URL: {profile_url}")

        # Wait until the followers link is clickable
        # NOTE: XPath may change if Instagram updates their DOM
        followers_link_xpath = (
            '//header//ul/li[2]//a[contains(@href,"/followers")]//span'
        )
        followers_link = self.wait_for_element(By.XPATH, followers_link_xpath)
        followers_link.click()
        logging.info("Clicked on followers link")

        # Wait for followers popup container to appear
        try:
            popup_xpath = '//div[@role="dialog"]//div[@aria-label="Followers"]'
        except Exception as e:
            popup_xpath = '<div aria-level="1" class="" role="heading">Followers</div>'
        popup_container = self.wait_for_element(By.XPATH, popup_xpath)
        logging.info("Followers popup appeared")

        # Scroll the followers popup to load more followers
        for _ in range(30):  # Adjust number of scrolls as needed
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                popup_container,
            )
            time.sleep(random.uniform(1, 2))
        logging.info("Completed scrolling followers list")

        # Locate follower "Follow" buttons inside popup
        # WARNING: XPath is subject to change if Instagram layout updates
        buttons_xpath = (
            './/button[text()="Follow" or text()="Follow Back"]'
        )
        follow_buttons = popup_container.find_elements(By.XPATH, buttons_xpath)
        logging.info(f"Found {len(follow_buttons)} follow buttons to process")

        # Call follow method to click follow buttons
        self.follow(follow_buttons)

        # Optionally close the followers tab and switch back
        self.driver.close()
        self.driver.switch_to.window(original_tab)
        logging.info("Closed followers tab and switched back to original tab")

    def follow(self, buttons):
        """
        Iterate over a list of follow button elements and click them with human-like behavior.

        Args:
            buttons: List of WebElement buttons to click.
        """
        logging.info("Starting to follow users...")
        self.human_scroll(to="top")

        for idx, button in enumerate(buttons):
            try:
                button.click()
                logging.info(f"Clicked follow on user #{idx + 1}")
                # Simulate human mouse movement and scroll a bit
                self.human_mouse_movement()
                self.driver.execute_script("window.scrollBy(0, 70);")
                # Random pause between follow clicks to avoid detection
                time.sleep(random.uniform(2, 4))
            except Exception as e:
                logging.warning(f"Failed to click follow button #{idx + 1}: {e}")
                continue

    def quit(self):
        """
        Close the browser session cleanly.
        """
        self.driver.quit()
        logging.info("WebDriver session ended, browser closed.")

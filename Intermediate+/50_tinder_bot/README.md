
# Tinder Facebook Login Automation  
Automate Tinder login via Facebook using Selenium WebDriver, perform profile liking with handling for popups.

## Prerequisites
* **Install Selenium:** `pip install selenium`  
* **Install python-dotenv:** `pip install python-dotenv`  
* **ChromeDriver:** Ensure ChromeDriver is installed and matches your Chrome browser version  
* **Create a `.env` file:** Store your Facebook credentials securely  
  ```
  FACEBOOK_EMAIL=your_email@example.com
  FACEBOOK_PASSWORD=your_password
  ```

## Setup
* Configure ChromeDriver path in your environment if not added already  
* Run the script to launch Tinder, login via Facebook popup, then automate profile liking  
* The script uses environment variables for Facebook login credentials, and keeps browser open after run  


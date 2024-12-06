# LinkedIn Job Application Automation
Automate LinkedIn login and apply to jobs using Selenium WebDriver with handling for dynamic elements and simple application flows.

## Prerequisites
* **Install Selenium:**  
  `pip install selenium`  
* **Install python-dotenv:**  
  `pip install python-dotenv`  
* **ChromeDriver:**  
  Make sure ChromeDriver is installed and matches your Chrome browser version.  
* **Create a `.env` file:**  
  Store your LinkedIn credentials and phone number securely:  
  ```
  LINKEDIN_EMAIL=your_email@example.com
  LINKEDIN_PASSWORD=your_password
  LINKEDIN_PHONE=your_phone_number
  ```

## Setup
* Optionally add ChromeDriver to system PATH or specify its location in the script.  
* Run the script to:  
  - Open LinkedIn Jobs page  
  - Log in automatically  
  - Iterate over job listings and apply where possible  
  - Handle simple application modals, skip complex ones  
* The script uses environment variables for your credentials and keeps the browser open after execution for review.

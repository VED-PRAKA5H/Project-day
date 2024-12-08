# Instagram Followers Automation
Automate Instagram login and follower interaction using Selenium WebDriver. The script logs into Instagram, 
navigates to a target account, and can scroll and interact with followers in a human-like way.

## Prerequisites
- **Install Selenium:** `  pip install selenium  `
- **Install python-dotenv:**  ` pip install python-dotenv`
- **ChromeDriver:** Download [ChromeDriver](https://chromedriver.chromium.org/) matching your installed Chrome browser version and add it to your PATH.
- **Create a `.env` file** to store your Instagram credentials securely:
  ```
  IG_USERNAME=your_instagram_username
  IG_PASSWORD=your_instagram_password
  ```

## Setup & Usage
1. Ensure ChromeDriver is accessible from your PATH or set the path explicitly in your script.
2. Update the `SIMILAR_ACCOUNT` variable in your script to the target account whose followers you wish to access.
3. Run the script: ` python main.py `
4. The script will:
   - Log in to Instagram with credentials from the `.env` file
   - Open the specified user’s followers list in a new tab
   - Scroll through and (optionally) follow users, simulating human behavior

# Password Manager

A simple password manager application with a Tkinter GUI to securely save and retrieve personal login credentials. Includes a password generator and uses the `pyperclip` package to facilitate clipboard copy functions.

***

### Features
- Generate strong random passwords of 20 characters including symbols, numbers, and letters.
- Save website, email/username, and password credentials in a JSON file.
- Search saved passwords by website.
- Pop-up message boxes for user feedback and confirmation.
- Clipboard functionality to copy generated passwords easily.
- Simple, easy-to-use graphical interface built with Tkinter.

***

### Technologies Used
- **Python 3**  
- **Tkinter** for the GUI  
- **pyperclip** module for clipboard copy and paste (ensure installed via pip)  
- JSON file handling to store credentials securely in a structured format.

***

### Installation

1. Make sure Python 3.x is installed.  
2. Install the `pyperclip` package if not installed:

    ```bash
    pip install pyperclip
    ```

3. Save the project files (`password_manager.py`, `logo.png`, etc.) to a directory.

***

### How to Use

1. Run the Python script:

    ```bash
    python main.py
    ```

2. Enter the website name in the **Website** field (default example: groww.com).  
3. Enter the email or username associated with the website (default example given: ved@gmail.com).  
4. Generate a strong password by clicking **Generate Password** or enter one manually. Generated passwords are copied to clipboard automatically.  
5. Click **Add** to save the credentials. Confirmation pop-ups will appear.  
6. Use **Search** to find saved credentials by website and view email and password in a pop-up window.

***

### File Storage

Passwords and credentials are saved in a local `passwords.json` file in the format:

```json
{
    "website_name": {
        "email": "email_address",
        "password": "password_value"
    }
}
```

***

### Code Overview
- **Password Generator**: Random ASCII character generation for strong passwords.  
- **Save Password**: Validates inputs and stores data in JSON format, updating existing records safely.  
- **Show Password**: Reads JSON data and displays credentials for a given website.  
- **Clipboard**: Generated passwords are copied automatically for user convenience.  
- **UI Components**: Tkinter widgets arranged in grid layout; includes entry fields, buttons, labels, and canvas for logo.

***

### References
- [Pyperclip Documentation](https://pypi.org/project/pyperclip/)  
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  


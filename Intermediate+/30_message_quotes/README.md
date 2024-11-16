# Random Quote Messenger

A simple Python script to email random quotes to your friends daily, using the `smtplib` library for SMTP email sending.

***

### Features
- Sends a randomly selected quote from a text file via email.
- Uses Python's built-in `smtplib` for SMTP email communication.
- Securely loads email credentials from a `.env` file for security.
- Displays the current weekday in the email subject line.
- Lightweight and easy to customize with your own quotes and recipients.

***

### Requirements
- Python 3.x  
- `python-dotenv` package for environment variable management:

```bash
pip install python-dotenv
```

***

### Setup

1. Create a `.env` file in the project root directory with your email credentials:

    ```
    EMAIL=your_email@example.com
    PASSWORD=your_email_password
    ```

2. Prepare a `quotes.txt` file containing one quote per line (can include quotes with or without double quotes).

***

### How to Run

Run the script using:

```bash
python main.py
```

The script will:
- Load your email and password from the `.env` file.
- Pick a random quote from `quotes.txt`.
- Send an email with the quote as the message body to your recipient's email address.
- The email subject shows "Quote of the <Weekday>", e.g., "Quote of the Monday".

***

### Code Overview

- Uses `datetime` to get current weekday for subject line.  
- Reads quotes from `quotes.txt` and selects one randomly.  
- Loads sensitive information securely from `.env`.  
- Connects to Gmail's SMTP server with TLS encryption.  
- Logs in and sends the email with the generated message.

***

### Security Notes

- Keep your `.env` file private and excluded from version control (.gitignore).  
- Use app-specific passwords or OAuth tokens for Gmail to improve security.  
- Avoid storing plain-text passwords in scripts.

***

### References

- [smtplib official Python documentation](https://docs.python.org/3/library/smtplib.html)  
- [python-dotenv PyPI page](https://pypi.org/project/python-dotenv/)  

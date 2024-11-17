# Birthday Wisher

A Python script that automatically sends birthday wishes via email to people whose birthday is on the current date.

***

### Features
- Checks a CSV file with birthdays to find matching birthdays for today.  
- Uses randomly selected personalized letter templates for the birthday message.  
- Sends emails securely using Gmail's SMTP server and TLS encryption.  
- Environment variables in a `.env` file store sensitive email credentials for security.  
- Graceful error handling for missing files and SMTP exceptions.

***

### Requirements
- Python 3.x  
- `pandas` library for CSV file reading:

```bash
pip install pandas
```

- `python-dotenv` package for environment variable loading:

```bash
pip install python-dotenv
```

***

### Setup

1. Create a `.env` file in your project root with your email and password:

    ```
    EMAIL=your_email@example.com
    PASSWORD=your_app_password
    ```

2. Prepare a `birthdays.csv` file in the root directory in this format:
    
    | name       | email              | year | month | day |
    |------------|--------------------|------|-------|-----|
    | John Smith | john@example.com   | 1990 | 9     | 13  |

3. Put letter templates named `letter_1.txt`, `letter_2.txt`, `letter_3.txt` in the folder `letter_templates/`. In these templates, use `[NAME]` as a placeholder for the recipient's name.

***

### How to Run

Simply execute:

```bash
python birthday_wisher.py
```

The script will:
- Read today's date.
- Check the birthdays CSV for matches.
- For each matching birthday, pick a random letter template.
- Personalize it with the person's name.
- Send the birthday email.

***

### Code Overview

- Loads `.env` for credentials.  
- Reads birthday data CSV with pandas.  
- Compares current date with entries.  
- Reads one of 3 letter templates randomly.  
- Sends email via Gmail SMTP with `smtplib`.  
- Includes error handling for missing files and SMTP errors.

***

### Security Notes

- Keep `.env` private and excluded from public repositories.  
- For Gmail, create an app-specific password if 2FA is enabled and do not use your primary password directly.  
- Never share your `.env` file or passwords in code or public repos.

***

### References

- [Python smtplib documentation](https://docs.python.org/3/library/smtplib.html)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  
- [Pandas documentation](https://pandas.pydata.org/)  

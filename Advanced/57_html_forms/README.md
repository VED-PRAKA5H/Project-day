# Flask Registration Form with SMTP Email Notification

A responsive user registration form built with Flask that sends HTML-formatted email notifications via SMTP when users submit the form.

## Features

- Multi-section form with validation and accessibility
- Flask backend handling form submissions
- Email notifications using `smtplib` with HTML email templates
- Configured via environment variables (`.env`)
- Mobile-friendly and styled with CSS animations

## Flask Request Details

- The registration form submits data via an HTTP **POST** request to the `/register` route.
- The Flask backend accesses the submitted form data using the `request` object from `flask`:
  ```python
  @app.route('/register', methods=['POST'])
  ```
- This approach securely captures and processes user inputs sent from the frontend form.

- Using request.form.get() safely retrieves data, returning None if a field is missing, avoiding KeyErrors.
***

You can add this after your **Usage** or **Code Highlights** section for clarity. Let me know if you want me to integrate it fully into the README!

## Project Structure

```text
registration-flask-project/
│
├── templates/
│   ├── index.html
│   ├── success.html
│
├── static/
│   └── style.css
│
├── mail_sender.py        # SMTP email sender module
├── main.py               # Flask app with routes and logic
├── requirements.txt
├── .env                  # Environment variables (not committed)
├── README.md
```

## Setup

1. Clone and navigate to project folder.  

2. Create `.env` file with SMTP credentials:

   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   MAIL_DEFAULT_SENDER=your_email@gmail.com
   ```
3. Run the app:

   ```bash
   flask run
   ```

Access at `http://127.0.0.1:5000`

## Usage

- Fill the form, submit, and receive a success message.
- The app sends an HTML email notification with user details via SMTP.

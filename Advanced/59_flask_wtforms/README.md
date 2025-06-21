# Flask Login App  

A simple Flask web application with a login form built using **Flask**, **Flask-WTF**, and **Flask-Bootstrap4**. The app demonstrates form handling, template rendering, and basic authentication logic.  

***

### Features
- **Flask-WTF form handling** with validation.  
- **Flask-Bootstrap4 integration** for styling forms and pages.  
- Simple login system with hardcoded credentials:  
  - Email: `admin@email.com`  
  - Password: `12345678`  
- Redirects authenticated users to a success page.  
- Displays an access denied page for incorrect login attempts.  

***

### Project Structure
```text
project/
├── main.py                # Main Flask application
├── forms.py              # Form definitions (FlaskForm)
├── templates/            # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── success.html
│   └── denied.html
└── requirements.txt      # Python dependencies
```

***

### Installation  

1. Clone the repository:

2. Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

***

### Usage  

1. Run the development server:  
   ```bash
   python app.py
   ```

2. Open the app in your browser:  
   ```
   http://127.0.0.1:5000/
   ```

3. Navigate to the login page:
   ```
   http://127.0.0.1:5000/login
   ```

4. Test the login with:  
   - **Email:** `admin@email.com`  
   - **Password:** `12345678`  

***

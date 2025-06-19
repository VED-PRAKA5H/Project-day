from flask import Flask, render_template, request, redirect, url_for
from mail_sender import GmailSender  # Custom mail sender module

app = Flask(__name__)  # Initialize Flask app
gs = GmailSender()  # Create an instance of GmailSender to send emails


@app.route('/')
def home():
    """
    Route for the home page.
    Renders the registration form (index.html).
    """
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def login():
    """
    Route to handle form submission from the registration page.
    Accepts POST requests with user registration data.
    """
    try:
        # Extract form data from the request
        form_data = {
            'first_name': request.form.get('firstName'),
            'last_name': request.form.get('lastName'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'birthdate': request.form.get('birthdate'),
            'address': request.form.get('address'),
            'city': request.form.get('city'),
            'country': request.form.get('country'),
            'gender': request.form.get('gender'),
            'interests': request.form.getlist('interests'),  # Multiple values
            'bio': request.form.get('bio'),
            'website': request.form.get('website'),
            'newsletter': request.form.get('newsletter'),
            'terms': request.form.get('terms')
        }

        # Send the email using GmailSender instance
        gs.send_mail(user_detail=form_data)

        # If successful, redirect user to a success page
        return redirect(url_for('success'))

    except Exception as e:
        # On error, redirect back to the registration form page
        print(e)
        return redirect(url_for('home'))


@app.route('/success')
def success():
    """
    Route for the success page shown after successful registration/email sending.
    """
    return render_template('success.html')


if __name__ == '__main__':
    # Run the Flask app in debug mode (useful for development)
    app.run(debug=True)

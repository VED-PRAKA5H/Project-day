import os
import requests
from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
from send_mail import GmailSender

load_dotenv()
app = Flask(__name__)
current_year = datetime.today().year
npoint_id = os.getenv("NPOINT_BLOG")
try:
    response = requests.get(url=f"https://api.npoint.io/{npoint_id}")
    data = response.json()
except Exception as e:
    print("API ERROR", e)
    quit()
gs = GmailSender()


@app.route("/")
def home():
    return render_template('index.html', year=current_year, posts=data)


@app.route("/about")
def about():
    return render_template('about.html', year=current_year)


@app.route("/contact", methods=['GET', "POST"])
def contact():
    if request.method == 'POST':
        form_data = {
            'Name': request.form.get('name'),
            'Email': request.form.get('email'),
            'Phone': request.form.get('phone'),
            'Message': request.form.get('message'),
        }
        details = ""
        for key, value in form_data.items():
            details += f"{key}: {value}\n"
        gs.send_mail(user_detail=details)
        return render_template('success.html', year=current_year)

    else:
        return render_template('contact.html', year=current_year)


@app.route("/post/<num>")
def get_post(num):
    return render_template('post.html', posts=data, post_no=int(num), year=current_year)


if __name__ == "__main__":
    app.run(debug=True)

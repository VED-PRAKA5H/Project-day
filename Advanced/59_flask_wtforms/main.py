from flask import Flask, render_template, redirect, url_for, request
from forms import MyForm
from flask_bootstrap import Bootstrap4
app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        if form.user_email.data == "admin@email.com" and form.user_password.data == "12345678":

            return render_template('success.html')
        else:
            return render_template("denied.html")
    else:
        return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

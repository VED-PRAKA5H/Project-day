from flask import Flask
from random import randint

# Generate a random target number between 0 and 9 when the server starts
number_to_guess = randint(0, 9)

# Initialize the Flask web application
app = Flask(__name__)


# Decorator to center-align any HTML returned by a function
def center_div(function):
    def wrapper():
        tag = function()  # Get the HTML returned by the decorated function
        # Return that HTML wrapped in a centered <div>
        return f"<div style='text-align: center;'>{tag}</div>"

    return wrapper


# Home route: displays instructions, wrapped and centered using center_div decorator
@app.route("/")
@center_div
def home():
    return ("<h1>Guess the number between 0 and 9</h1>"
            "<p>Enter your answer in URL like this <b>http://127.0.0.1:5000/4</b> "
            "that is, write your guess after slash.</p>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


# Route for handling guesses; dynamically matches integers in the URL (e.g., /4)
@app.route("/<int:number>")
def guess(number):
    if number == number_to_guess:
        # Correct guess: display a green congratulatory message and corresponding gif
        return ("<h1 style='text-align: center; color:green'>You are right</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' "
                "style='display: block; margin-left: auto; margin-right: auto; width=200px'>")
    elif number > number_to_guess:
        # Guess is too high: blue message and a gif
        return ("<h1 style='text-align: center; color:blue'>Too high</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' "
                "style='display: block; margin-left: auto; margin-right: auto; width=200px'>")
    else:
        # Guess is too low: red message and a different gif
        return ("<h1 style='text-align: center; color:red'>Too low</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' "
                "style='display: block; margin-left: auto; margin-right: auto; width=150px'>")


# Run the Flask app if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    app.run()

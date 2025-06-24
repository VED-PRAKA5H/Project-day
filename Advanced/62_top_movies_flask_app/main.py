from flask import Flask, render_template, redirect, url_for, request
from movies_db import (init_app, create_tables, list_movies, add_movie, update_movie_rating, delete_movie,
                       get_movie_name_by_id, movie_id_by_name)
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from movie_api import get_movies_list_tmdb

# Create Flask app instance
app = Flask(__name__)

# Set secret key for WTForms CSRF protection and session management
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Initialize Bootstrap integration with Flask app for styling
Bootstrap5(app)

# Initialize database with Flask app configuration
init_app(app)

# Global list to hold movie data fetched from TMDB API during runtime
tmdb_movies = []


# ---------------------
# FORMS FOR USER INPUT
# ---------------------

class MovieForm(FlaskForm):
    """
    Form for entering a movie name to search and add.
    """
    title = StringField(label="Movie name", validators=[DataRequired()])
    submit_btn = SubmitField(label="Add Movie")


class EditMovieForm(FlaskForm):
    """
    Form to update a movie's rating and review.
    """
    new_rating = FloatField(
        label='Your rating out of 10',
        validators=[DataRequired(), NumberRange(0, 10)],
        render_kw={"placeholder": "e.g. 7.5"}
    )
    new_review = StringField(
        label='New movie review',
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your review"}
    )
    submit_btn = SubmitField(label="Update")


# --------------------
# ROUTES / ENDPOINTS
# --------------------

@app.route("/")
def home():
    """
    Home page route: show all movies in the database sorted by ranking.
    """
    movies_list = list_movies()
    return render_template("index.html", movies=movies_list)


@app.route("/add", methods=["POST", "GET"])
def add_movie_route():
    """
    Route to handle adding a new movie.
    - GET: Show form to enter movie name.
    - POST: Search TMDB for matching movies and show selection page.
    """
    if request.method == "POST":
        all_movies_tmdb = get_movies_list_tmdb(request.form.get('title'))
        if all_movies_tmdb is None:
            all_movies_tmdb = []
        # Store TMDB search results in global variable for later selection
        global tmdb_movies
        tmdb_movies = all_movies_tmdb
        # Render page for user to select the exact movie from search results
        return render_template('select.html', movies=all_movies_tmdb)
    else:
        # GET request: show empty form to input movie name
        add_movie_form = MovieForm()
        return render_template("add.html", form=add_movie_form)


@app.route("/edit", methods=["GET", "POST"])
def edit_route():
    """
    Route to edit a movie's rating and review.
    - GET: Display form with movie name.
    - POST: Process form submission and update data in DB.
    """
    movie_id = request.args.get("movie_id")
    if request.method == "POST":
        rating = request.form.get("new_rating")
        review = request.form.get("new_review")
        update_movie_rating(movie_id=int(movie_id), new_rating=float(rating), new_review=review)
        return redirect(url_for("home"))

    # GET request: render form for updating movie rating/review
    edit_movie_form = EditMovieForm()
    movie_name = get_movie_name_by_id(int(movie_id))
    return render_template('edit.html', form=edit_movie_form, movie_name=movie_name)


@app.route("/delete")
def delete_route():
    """
    Route to delete a movie by its ID.
    """
    movie_id = request.args.get("movie_id")
    delete_movie(movie_id=int(movie_id))
    return redirect(url_for("home"))


@app.route("/find")
def find_route():
    """
    Route to finalize adding a selected movie from TMDB search results:
    - Finds the selected movie by TMDB ID in the previously stored results.
    - Adds it to the local DB.
    - Redirects to editing form to add rating/review.
    """
    movie_id = request.args.get("id_")

    for m in tmdb_movies:
        if m.get('id') == int(movie_id):
            # Prepare movie data dictionary for insertion, correcting image URL path
            data = {
                "title": m.get("title"),
                "year": m.get("release_date"),
                "description": m.get("overview"),
                "rating": None,  # Initial rating is None (can be updated later)
                "ranking": None,  # Initial ranking is None (will be adjusted)
                "review": None,  # Initial review is None
                "img_url": f"https://image.tmdb.org/t/p/original{m.get('poster_path')}",
            }
            # Add movie record to the database
            add_movie(**data)
            # Retrieve new movie ID for editing
            id_ = movie_id_by_name(m.get("title"))
            return redirect(url_for('edit_route', movie_id=id_))

    # If movie not found, redirect back to home page
    return redirect(url_for('home'))


# ------------------
# APP ENTRY POINT
# ------------------

if __name__ == '__main__':
    # Create tables if they do not exist before running server
    with app.app_context():
        create_tables()
    # Start Flask development server with debug mode enabled
    app.run(debug=True)

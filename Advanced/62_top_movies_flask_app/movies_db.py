from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, VARCHAR


# ----------------------
# DATABASE CONFIGURATION
# ----------------------

# Base class for SQLAlchemy ORM models
class LibraryBase(DeclarativeBase):
    pass


# Create a SQLAlchemy object configured with our custom Base
db = SQLAlchemy(model_class=LibraryBase)


def init_app(app) -> None:
    """
    Attach SQLAlchemy database settings to a Flask app instance.
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"  # SQLite file-based DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable change tracking overhead
    db.init_app(app)  # Bind DB to Flask app


# -------------
# ORM MODEL
# -------------

class Movie(db.Model):
    """
    ORM model representing a Movie table in the database.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key
    title: Mapped[str] = mapped_column(VARCHAR, unique=True, nullable=False)  # Movie title (must be unique)
    year: Mapped[str] = mapped_column(String(200), nullable=False)  # Release year or date
    description: Mapped[str] = mapped_column(String(250), nullable=False)  # Short description/summary
    rating: Mapped[float] = mapped_column(Float, nullable=True)  # User rating, can be NULL
    ranking: Mapped[str] = mapped_column(Integer, nullable=True)  # Rank based on rating, can be NULL
    review: Mapped[str] = mapped_column(String(250), nullable=True)  # Personal review/notes
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # Poster/cover image URL


# ----------------
# SERVICE FUNCTIONS
# ----------------

def create_tables() -> None:
    """
    Create all database tables if they don't exist already.
    """
    db.create_all()
    print("✅ Tables created successfully.")


def add_movie(title: str, year: str, description: str, rating, ranking, review, img_url: str) -> None:
    """
    Add a new movie record into the database.
    """
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url,
    )
    db.session.add(new_movie)  # Stage the new movie for insertion
    db.session.commit()  # Commit the transaction to save it
    print(f"✅ Added '{title}' movie")


def list_movies() -> list[dict]:
    """
    Retrieve all movies from the database, sorted by ranking (highest first),
    and return them as a list of dictionaries.
    """
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.ranking.desc())
    ).scalars().all()

    return [
        {
            "id": m.id,
            "title": m.title,
            "year": m.year,
            "description": m.description,
            "rating": m.rating,
            "ranking": m.ranking,
            "review": m.review,
            "img_url": m.img_url
        }
        for m in movies
    ]


def adjust_ranking():
    """
    Adjust movie rankings based on rating:
    - Sorts movies in ascending order of rating
    - Assigns highest ranking to the movie with highest rating
    """
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.rating)
    ).scalars().all()

    top_rank = len(movies)
    for m in movies:
        update_ranking(m.id, top_rank)
        top_rank -= 1
    print("🎯 Rankings adjusted")


def update_movie_rating(movie_id: int, new_rating: float, new_review: str) -> None:
    """
    Update the rating and review for a given movie by its ID.
    Also triggers re-ranking of all movies.
    """
    movie = db.session.execute(
        db.select(Movie).where(Movie.id == movie_id)
    ).scalar()

    if movie:
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        print(f"✅ Updated rating for '{movie.title}' → {new_rating}")
        adjust_ranking()


def update_ranking(movie_id: int, new_ranking: int) -> None:
    """
    Update the ranking for a given movie by its ID.
    """
    movie = db.session.execute(
        db.select(Movie).where(Movie.id == movie_id)
    ).scalar()

    if movie:
        movie.ranking = new_ranking
        db.session.commit()


def delete_movie(movie_id: int) -> None:
    """
    Delete a movie record from the database by its ID.
    """
    movie = db.get_or_404(Movie, movie_id)  # Fetch or return 404 if not found
    print(f"🗑️ Deleted '{movie.title}'")
    db.session.delete(movie)
    db.session.commit()


def get_movie_name_by_id(movie_id: int) -> str:
    """
    Retrieve the movie title for a given movie ID.
    """
    movie = db.get_or_404(Movie, movie_id)
    return movie.title


def movie_id_by_name(movie_name: str) -> int:
    """
    Retrieve the movie ID for a given title.
    """
    movie = db.session.execute(
        db.select(Movie).where(Movie.title == movie_name)
    ).scalar()
    return movie.id

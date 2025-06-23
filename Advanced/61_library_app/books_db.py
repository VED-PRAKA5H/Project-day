from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, VARCHAR


# DB CONFIGURATION
class LibraryBase(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=LibraryBase)


def init_app(app) -> None:
    """Attach database settings to Flask app."""
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


# ORM MODEL
class Book(db.Model):
    """ORM model representing a Book table."""
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# SERVICE FUNCTIONS
def create_tables() -> None:
    """Create database tables if not exist."""
    db.create_all()
    print("✅ Tables created successfully.")


def add_book(title: str, author: str, rating: float) -> None:
    """Add a new book into the DB."""
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()
    print(f"✅ Added '{title}' by {author}")


def list_books() -> list[dict]:
    """Return list of all books."""
    books = db.session.execute(db.select(Book)).scalars().all()
    return [
        {"ID": b.id, "Title": b.title, "Author": b.author, "Rating": b.rating}
        for b in books
    ]


def update_book_rating(book_id: int, new_rating: float) -> None:
    """Update rating for a given book ID."""
    book = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    if book:
        book.rating = new_rating
        db.session.commit()
        print(f"✅ Updated rating for '{book.title}' → {new_rating}")

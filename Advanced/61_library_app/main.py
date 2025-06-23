from flask import Flask, render_template, request, redirect, url_for
from books_db import init_app, create_tables, list_books, add_book, update_book_rating

app = Flask(__name__)
init_app(app)


# HOME ROUTE
@app.route('/')
def home():
    """Display all books."""
    return render_template('index.html', book_data=list_books())


# ADD BOOK ROUTE
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        add_book(
            title=request.form.get('book_name'),
            author=request.form.get('book_author'),
            rating=float(request.form.get('reader_rating'))
        )
        return redirect(url_for('home'))
    return render_template('add.html')


# EDIT RATING ROUTE
@app.route('/edit', methods=['GET', 'POST'])
def edit_rating():
    book_id = int(request.args.get('book_id'))
    if request.method == 'POST':
        update_book_rating(book_id, float(request.form.get('new_rating')))
        return redirect(url_for('home'))

    # GET → show update form
    for book in list_books():
        if book["ID"] == book_id:
            return render_template('update.html', row=book)


# MAIN ENTRY POINT
if __name__ == "__main__":
    with app.app_context():
        create_tables()
    app.run(debug=True)

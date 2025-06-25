# Import necessary libraries
from sqlalchemy.exc import IntegrityError  # To handle duplicate entries or SQL constraints
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, update, delete, insert
from random import choice

# Initialize Flask application
app = Flask(__name__)


# -------------------- DATABASE SETUP --------------------

# Base class for SQLAlchemy models using Declarative Mapping
class Base(DeclarativeBase):
    pass


# Connect to SQLite database file 'cafes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe table model definition with SQLAlchemy and Python typing
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


# Create the tables in the database if they don't exist
with app.app_context():
    db.create_all()


# -------------------- HELPER FUNCTION --------------------

def get_cafe_list(by=None, value=None):
    """
    Fetch list of cafes.
    If 'by' and 'value' are provided, filter cafes by that column name and value.
    Returns the list as dictionaries for easy JSON conversion.
    """
    if by is None or value is None:
        cafes = db.session.execute(
            db.select(Cafe)
        ).scalars().all()
    else:
        cafes = db.session.execute(
            db.select(Cafe).where(getattr(Cafe, by) == value)
        ).scalars().all()

    cafes_list = []
    for cafe in cafes:
        cafes_list.append({
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        })
    return cafes_list


# -------------------- ROUTES --------------------

@app.route("/")
def home():
    """Render the home page (HTML template)."""
    return render_template("index.html")


# ---------- HTTP GET: Retrieve Data ----------

@app.route('/random', methods=["GET"])
def get_record():
    """Return a random cafe from the database in JSON format."""
    cafes_list = get_cafe_list()
    return jsonify({"cafe": choice(cafes_list)})


@app.route("/all", methods=["GET"])
def get_all():
    """Return all cafes in the database."""
    return jsonify({'cafes': get_cafe_list()})


@app.route("/search", methods=["GET"])
def search_cafe():
    """
    Search cafes by location.
    Example: /search?loc=London
    """
    loc = request.args.get("loc")
    cafes_list = get_cafe_list(by="location", value=loc)

    if not cafes_list:
        return jsonify({"error": {"Not found": "Sorry, we don't have any cafe at that location."}})
    else:
        return jsonify({'cafes': cafes_list})


# ---------- HTTP POST: Create Data ----------

@app.route("/add", methods=["POST"])
def add_cafe():
    """
    Add a new cafe to the database.
    Requires API key in query string: ?api-key=TopSecretAPI987686
    Accepts JSON body with cafe details.
    """
    if request.args.get('api-key') == "TopSecretAPI987686":
        cafe_details = request.get_json()
        try:
            stmt = insert(Cafe).values(**cafe_details)
            db.session.execute(stmt)
            db.session.commit()
            db.session.close()
            return jsonify({
                "status": 200,
                "response": f"Successfully added the new cafe at location {cafe_details['location']}"
            })
        except IntegrityError:
            # Cafe name must be unique, if duplicate -> IntegrityError
            return jsonify({
                "status": 200,
                "response": "The Cafe is already in the database."
            })
    else:
        return jsonify({
            "status": 200,
            "response": "Incorrect API key"
        })


# ---------- HTTP PATCH: Update Data ----------

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    """
    Update the coffee price of an existing cafe by ID.
    Requires query parameter: ?new_price=<price>
    """
    price = request.args.get("new_price")
    try:
        stmt = update(Cafe).where(Cafe.id == cafe_id).values(coffee_price=price)
        db.session.execute(stmt)
        db.session.commit()
        db.session.close()
        return jsonify({
            "status": 200,
            "response": "Successfully updated the cafe price."
        })
    except Exception:
        return jsonify({
            "status": 200,
            "response": "Sorry, no cafe found with that ID."
        })


# ---------- HTTP DELETE: Delete Data ----------

@app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete_a_row(cafe_id):
    """
    Delete a cafe entry by ID (mark as closed).
    Requires 'api-key' in request headers.
    """
    apikey = request.headers.get('api-key')
    if apikey == 'abcd1234':
        try:
            stmt = delete(Cafe).where(Cafe.id == cafe_id)
            db.session.execute(stmt)
            db.session.commit()
            db.session.close()
            return jsonify({
                "status": 200,
                "response": f"Successfully deleted cafe with ID {cafe_id}."
            })
        except Exception as e:
            return jsonify({
                "status": 200,
                "response": f"Sorry, cafe not found. {e}"
            })
    else:
        return jsonify({
            "status": 200,
            "response": "Incorrect API key"
        })


# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)

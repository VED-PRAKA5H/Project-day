from flask import Flask, render_template
from datetime import datetime
from post import Post  # Imports your Post class which fetches the posts

# Create a new Flask application
app = Flask(__name__)

# Get the current year for use in the footer or elsewhere
year = datetime.today().year

try:
    # Instantiate the Post object and retrieve all blog posts
    post = Post()
    blog_post = post.posts
except Exception as e:
    print(f"Failed to load posts: {e}")
    blog_post = []


@app.route("/")
def home():
    """
    Route for the home page.
    Renders the main blog index with a list of all posts.

    Passes:
        - posts: list of all blog posts for displaying summaries
        - current_year: the current year, for dynamic copyright/footer
    """
    return render_template(
        "index.html",
        posts=blog_post,
        current_year=year
    )


@app.route("/blog/<num>")
def get_blog(num):
    """
    Route for individual blog post pages.

    Args:
        num (str): The unique post identifier (typically an int as a string)

    Passes:
        - posts: all blog post data (template will select by id)
        - current_year: for dynamic footer
        - post_number: the numeric post id for display logic in the template

    Handles:
        - If the post number is invalid (not int), triggers a 404 via Flask.
    """
    try:
        post_number = int(num)
    except ValueError:
        # If the num is not a valid integer, you might want to handle it (e.g., return 404)
        return "Post not found", 404

    return render_template(
        'post.html',
        posts=blog_post,
        current_year=year,
        post_number=post_number
    )


if __name__ == "__main__":
    # Run the Flask development server with debug mode enabled
    app.run(debug=True)


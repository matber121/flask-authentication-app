from flask import Blueprint, render_template

# Create the Blueprint for views (home page, etc.)
views = Blueprint('views', __name__)

# Route for the home page
@views.route('/')
def home():
    return render_template("home.html")

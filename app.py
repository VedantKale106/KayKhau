from datetime import datetime
import re
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pytz
from urllib.parse import unquote

# Load environment variables from .env file
load_dotenv()

# Get values from the .env file
SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URI = os.getenv("MONGO_URI")

# Flask application setup
app = Flask(__name__)
app.secret_key = SECRET_KEY

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client.food_app
food_collection = db.foods
users_db = db.users
visits_db = db.visits  # Creating a collection for storing visit data

# Helper function to get IST time
def get_ist_time():
    # Define Indian Standard Time (IST) timezone
    IST = pytz.timezone('Asia/Kolkata')
    # Get the current time in UTC and convert it to IST
    return datetime.now(IST)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Query the database to find the user by username
        user = users_db.find_one({"username": username})
        
        # Check if user exists and if the password matches
        if user and user["password"] == password:
            session["user"] = username  # Store username in session
            
            # Store the visit information
            visit_time = get_ist_time()
            visits_db.insert_one({"username": username, "time": visit_time})
            
            return redirect(url_for("homepage"))
        else:
            return "Invalid login. Please try again."
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Check if the username already exists in the users collection
        if users_db.find_one({"username": username}):
            return "Username already exists. Please choose a different username."
        
        # Ensure both username and password are provided
        if username and password:
            # Save user details in the MongoDB "users" collection
            users_db.insert_one({"username": username, "password": password})
            session["user"] = username  # Log the user in immediately
            
            # Store the visit information right after registration
            visit_time = get_ist_time()
            visits_db.insert_one({"username": username, "time": visit_time})
            
            return redirect(url_for("homepage"))
        else:
            return "Please fill in both fields."
    
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.clear()  
    
    return redirect(url_for('login'))

@app.route("/homepage")
def homepage():
    if "user" in session:
        food = food_collection.aggregate([{"$sample": {"size": 1}}])
        food = list(food)[0]
        return render_template("homepage.html", food=food)
    return redirect(url_for("login"))

@app.route("/food/<food_name>")
def food_details(food_name):
    # Decode the URL-encoded food name (to handle spaces and other special characters)
    decoded_food_name = unquote(food_name)
    food = food_collection.find_one({"name": decoded_food_name})
    return render_template("food_details.html", food=food)

@app.route("/all_foods", methods=["GET", "POST"])
def all_foods():
    query = {}
    if request.method == "POST":
        search_term = request.form["search"].strip()
        if search_term:
            # Create a case-insensitive regex pattern that matches words starting with the search term
            regex_pattern = f"\\b{re.escape(search_term)}"
            query = {
                "$or": [
                    {"name": {"$regex": regex_pattern, "$options": "i"}},
                    {"type": {"$regex": regex_pattern, "$options": "i"}},
                    {"description": {"$regex": regex_pattern, "$options": "i"}}
                ]
            }
    
    # Sort foods alphabetically by name
    foods = food_collection.find(query).sort("name", 1)
    return render_template("all_foods.html", foods=foods)

@app.route("/filter", methods=["GET", "POST"])
def filter_food():
    # Get unique values for dropdowns
    cuisine_types = sorted(food_collection.distinct("type"))
    landmark = sorted(food_collection.distinct("landmark"))
    
    # Initialize filters
    filters = {}
    selected_filters = {
        "selected_type": "",
        "selected_landmark": "",
        "selected_price": "",
        "selected_rating": "",
        "is_veg": False
    }
    
    if request.method == "POST":
        # Get filter values from form
        food_type = request.form.get("type")
        landmark = request.form.get("landmark")
        max_price = request.form.get("max_price")
        min_rating = request.form.get("min_rating")
        is_veg = request.form.get("veg") == "true"
        
        # Build filter query
        if food_type:
            filters["type"] = food_type
            selected_filters["selected_type"] = food_type
            
        if landmark:
            filters["landmark"] = landmark
            selected_filters["selected_landmark"] = landmark
            
        if max_price and max_price.isdigit():
            filters["price"] = {"$lte": int(max_price)}
            selected_filters["selected_price"] = max_price
            
        if min_rating:
            filters["rating"] = {"$gte": float(min_rating)}
            selected_filters["selected_rating"] = min_rating
            
        if is_veg:
            filters["veg"] = True
            selected_filters["is_veg"] = True
    
    # Get filtered foods, sorted by rating
    foods = food_collection.find(filters).sort([
        ("rating", -1),  # Sort by rating descending
        ("price", 1)     # Then by price ascending
    ])
    
    return render_template(
        "filter.html",
        foods=foods,
        cuisine_types=cuisine_types,
        landmark=landmark,
        **selected_filters
    )

if __name__ == "__main__":
    app.run(debug=True)

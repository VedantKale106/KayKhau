from datetime import datetime
import re
from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pytz
from urllib.parse import unquote

# Load environment variables from .env file
load_dotenv()

# Get values from the .env file
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Flask application setup
app = Flask(__name__)
app.secret_key = SECRET_KEY

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client.food_app
food_collection = db.foods
users_db = db.users
visits_db = db.visits  
feedback_collection = db.feedbacks 


# Helper function to get IST time
def get_ist_time():
    IST = pytz.timezone('Asia/Kolkata')
    return datetime.now(IST)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Query the database to find the user by username
        user = users_db.find_one({"username": username})

        if user and user["password"] == password:
            session["user"] = username  # Store username in session
            session.permanent = True  # Make session permanent

            # Store the visit information
            visit_time = get_ist_time()
            visits_db.insert_one({"username": username, "time": visit_time})

            return redirect(url_for("homepage"))
        else:
            flash("Invalid login. Please try again.", "error")
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if users_db.find_one({"username": username}):
            flash("Username already exists. Please choose a different username.", "error")
            return redirect(url_for("register"))

        if username and password:
            users_db.insert_one({"username": username, "password": password})
            session["user"] = username
            visit_time = get_ist_time()
            visits_db.insert_one({"username": username, "time": visit_time})
            return redirect(url_for("homepage"))
        else:
            flash("Please fill in both fields.", "error")

    return render_template("register.html")

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))

@app.route("/homepage")
def homepage():
    if "user" in session:
        food = food_collection.aggregate([{"$sample": {"size": 1}}])
        food = list(food)[0]
        return render_template("homepage.html", food=food, user=session["user"])
    flash("Please log in to access the homepage.", "error")
    return redirect(url_for("login"))

@app.route("/food/<food_name>")
def food_details(food_name):
    decoded_food_name = unquote(food_name)
    food = food_collection.find_one({"name": decoded_food_name})
    return render_template("food_details.html", food=food)

@app.route("/all_foods", methods=["GET", "POST"])
def all_foods():
    query = {}
    if request.method == "POST":
        search_term = request.form.get("search", "").strip()
        if search_term:
            regex_pattern = f"\\b{re.escape(search_term)}"
            query = {
                "$or": [
                    {"name": {"$regex": regex_pattern, "$options": "i"}},
                    {"type": {"$regex": regex_pattern, "$options": "i"}},
                ]
            }
    
    # Use aggregation with $match and $sample for random sorting
    foods_cursor = food_collection.aggregate([
        {"$match": query},  # Apply the search filter
        {"$sample": {"size": food_collection.count_documents(query)}}  # Randomize all matching documents
    ])
    
    # Convert the cursor to a list for rendering
    foods = list(foods_cursor)
    return render_template("all_foods.html", foods=foods)


@app.route("/filter", methods=["GET", "POST"])
def filter_food():
    # Get unique values for dropdowns
    cuisine_types = sorted(food_collection.distinct("type"))
    landmarks = sorted(food_collection.distinct("landmark"))  # Use `landmarks` here
    
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
        selected_landmark = request.form.get("landmark")  # Use `landmark` here to match the template
        max_price = request.form.get("max_price")
        min_rating = request.form.get("min_rating")
        is_veg = request.form.get("veg") == "true"
        
        # Build filter query
        if food_type:
            filters["type"] = food_type
            selected_filters["selected_type"] = food_type
            
        if selected_landmark:  # Use the variable `selected_landmark`
            filters["landmark"] = selected_landmark
            selected_filters["selected_landmark"] = selected_landmark
            
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
        landmarks=landmarks,  # Pass the corrected `landmarks` variable here
        **selected_filters
    )





@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        # Get form data
        dish = request.form.get("dish", "").strip()
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        feedback_text = request.form.get("feedback", "").strip()

        # Validate form data
        if not dish or not name or not phone or not feedback_text:
            flash("All fields are required.", "error")
            return redirect("/feedback")

        if len(phone) != 10 or not phone.isdigit():
            flash("Phone number must be a 10-digit number.", "error")
            return redirect("/feedback")

        # Save feedback to MongoDB
        feedback_data = {
            "dish": dish,
            "name": name,
            "phone": phone,
            "feedback": feedback_text
        }
        feedback_collection.insert_one(feedback_data)
        flash("Thank you for your feedback!", "success")
        return redirect("/feedback")

    return render_template("feedback.html")


@app.route("/hotels", methods=["GET", "POST"])
def hotels():
    if request.method == "POST":
        # Store the search term in the session for filtering later
        search_term = request.form.get("search", "").strip()
        session["search_term"] = search_term
        return redirect(url_for("hotels"))  # Redirect to the GET route
    
    # For GET requests, retrieve the search term from the session
    search_term = session.pop("search_term", "")
    query = {}
    if search_term:
        # Create a regex pattern to search for hotel names
        regex_pattern = f"\\b{re.escape(search_term)}"
        query = {"hotelname": {"$regex": regex_pattern, "$options": "i"}}
    
    # Fetch filtered hotels or all hotels if no search term
    hotels = food_collection.distinct("hotelname", query)
    return render_template("hotels.html", hotels=hotels)


@app.route("/hotel/<hotelname>", methods=["GET"])
def hotel_dishes(hotelname):
    dishes = food_collection.find({"hotelname": hotelname}).sort("name", 1)
    return render_template("hotel_dishes.html", hotelname=hotelname, dishes=dishes)

if __name__ == "__main__":
    app.run(debug=True)

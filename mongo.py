from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Adjust the URI if needed
db = client.food_app
food_collection = db.foods

# Delete all existing documents
food_collection.delete_many({})

# Dummy food data with the same image for all foods
food_data = [
    {
        "name": "Pasta Primavera",
        "location": "Pune",
        "hotelname": "Italian Delight",
        "type": "Italian",
        "rating": 4.5,
        "price": 250,
        "quantity": 1,
        "time": "20 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near Mall Road",
        "veg": True,
        "otheroptions": ["Extra Cheese", "Garlic Bread"]
    },
    {
        "name": "Chicken Biryani",
        "location": "Hyderabad",
        "hotelname": "Biryani House",
        "type": "Indian",
        "rating": 4.8,
        "price": 350,
        "quantity": 1,
        "time": "30 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near Charminar",
        "veg": False,
        "otheroptions": ["Extra Chicken", "Raita"]
    },
    {
        "name": "Veggie Burger",
        "location": "Mumbai",
        "hotelname": "Fast Food Corner",
        "type": "Fast Food",
        "rating": 4.0,
        "price": 120,
        "quantity": 1,
        "time": "15 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near CST",
        "veg": True,
        "otheroptions": ["Cheese Slice", "Spicy Sauce"]
    },
    {
        "name": "Paneer Tikka",
        "location": "Delhi",
        "hotelname": "Punjabi Tadka",
        "type": "Indian",
        "rating": 4.6,
        "price": 200,
        "quantity": 1,
        "time": "25 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near India Gate",
        "veg": True,
        "otheroptions": ["Mint Chutney", "Salad"]
    },
    {
        "name": "Margherita Pizza",
        "location": "Bangalore",
        "hotelname": "Pizza Point",
        "type": "Italian",
        "rating": 4.2,
        "price": 300,
        "quantity": 1,
        "time": "20 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near MG Road",
        "veg": True,
        "otheroptions": ["Extra Cheese", "Chili Flakes"]
    },
    # More food items added
    {
        "name": "Sushi Rolls",
        "location": "Tokyo",
        "hotelname": "Sushi Masters",
        "type": "Japanese",
        "rating": 4.7,
        "price": 500,
        "quantity": 1,
        "time": "40 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near Shibuya Crossing",
        "veg": False,
        "otheroptions": ["Wasabi", "Pickled Ginger"]
    },
    {
        "name": "Spaghetti Carbonara",
        "location": "Rome",
        "hotelname": "Pasta Heaven",
        "type": "Italian",
        "rating": 4.9,
        "price": 450,
        "quantity": 1,
        "time": "25 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near Colosseum",
        "veg": False,
        "otheroptions": ["Extra Parmesan", "Garlic Bread"]
    },
    {
        "name": "Falafel Wrap",
        "location": "Cairo",
        "hotelname": "Cairo Street Food",
        "type": "Middle Eastern",
        "rating": 4.3,
        "price": 180,
        "quantity": 1,
        "time": "10 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near Pyramids",
        "veg": True,
        "otheroptions": ["Hummus", "Tahini Sauce"]
    },
    {
        "name": "Tacos",
        "location": "Mexico City",
        "hotelname": "Taco Fiesta",
        "type": "Mexican",
        "rating": 4.6,
        "price": 120,
        "quantity": 1,
        "time": "15 minutes",
        "imageurl": "static/images/image.jpg",  # All foods have the same image
        "landmark": "Near Zocalo",
        "veg": True,
        "otheroptions": ["Guacamole", "Hot Sauce"]
    }
]

# Insert food data into MongoDB
food_collection.insert_many(food_data)
print("Food data inserted successfully!")

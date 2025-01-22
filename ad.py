import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Get values from the .env file
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client.food_app
food_collection = db.foods
# Delete all existing documents
food_collection.delete_many({})

# Dummy food data with the same image for all foods
food_data = [
    {
        "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/UGqcY1ocJHVq1EkRA",
        "hotelname": "Aaisaheb Mess",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/aaisaheb.jpg", 
        "landmark": "Mess Gully",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian foods"]
    },
    {
        "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/RNBrdZvUgWT7f6QA6",
        "hotelname": "Maitri Katta Mess",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/maitrikatta.jpg", 
        "landmark": "Mess Gully",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian foods"]
    },
    {
        "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/bGWSTA4fBRBik4EH6",
        "hotelname": "Maitri Katta Mess",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/image.jpg", 
        "landmark": "Mess Gully",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian foods"]
    },
    {
        "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/DVu2QAB5pxZxR5fW7",
        "hotelname": "Tuljabhavani Mess",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/image.jpg",  
        "landmark": "Mess Gully",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian foods"]
    },
    {
        "name": "Misal",
        "location": "https://maps.app.goo.gl/nF53Jh9QE2NXD4dg6",
        "hotelname": "PM Misal",
        "type": "Misal",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/pm.jpg", 
        "landmark": "Akurdi Railway Station",
        "veg": True,
        "otheroptions": ["Misal and Bhel"]
    },
    {
        "name": "Samosa Chaat",
        "location": "https://maps.app.goo.gl/MydWTqRE3VXhPimC6",
        "hotelname": "Krushnai Snacks",
        "type": "Chaat",
        "rating": 4.5,
        "price": 50,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/krushnai.png",  
        "landmark": "Akurdi Railway Station",
        "veg": True,
        "otheroptions": ["Pohe, Dal Pakwan"]
    },
    {
        "name": "Dalcha Rice",
        "location": "https://maps.app.goo.gl/MydWTqRE3VXhPimC6",
        "hotelname": "7 Mitranchi Dalcha Rice",
        "type": "Rice",
        "rating": 4.5,
        "price": 20,
        "quantity": 2,
        "time": "All Day",
        "imageurl": "static/images/image.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": True,
        "otheroptions": ["Nilanga Rice"]
    },
    {
        "name": "Chinese",
        "location": "https://maps.app.goo.gl/vQXqWYLiWNtwaTpSA",
        "hotelname": "Maharashtra Hotel",
        "type": "Chinese",
        "rating": 4.5,
        "price": 100,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/maharashtra.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": False,
        "otheroptions": ["Various Chinese Dishes"]
    },
    {
        "name": "Chicken Biryani",
        "location": "https://maps.app.goo.gl/vQXqWYLiWNtwaTpSA",
        "hotelname": "Maharashtra Hotel",
        "type": "Biryani",
        "rating": 4.5,
        "price": 120,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/maharashtra.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": False,
        "otheroptions": ["Veg Biryani"]
    },
    {
        "name": "Shawarma",
        "location": "https://maps.app.goo.gl/tYXA8HAHtsL9GnXm6",
        "hotelname": "Shawarma King",
        "type": "Shwarma",
        "rating": 4.5,
        "price": 150,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/shwarma.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": False,
        "otheroptions": ["Various Types of Shawarmas"]
    },
    {
        "name": "Medu Wada",
        "location": "https://maps.app.goo.gl/bxwvVCWqfnuiCvHw9",
        "hotelname": "Gangotree Fast Food",
        "type": "South Indian",
        "rating": 4.5,
        "price": 70,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/gangotree.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": True,
        "otheroptions": ["Idli, Dosa"]
    },
    {
        "name": "Veg Biryani",
        "location": "https://maps.app.goo.gl/bxwvVCWqfnuiCvHw9",
        "hotelname": "Gangotree Fast Food",
        "type": "Biryani",
        "rating": 4.5,
        "price": 70,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/gangotree.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": True,
        "otheroptions": ["Various Maharashtraian Dishes"]
    },
    {
        "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/bxwvVCWqfnuiCvHw9",
        "hotelname": "Gangotree Fast Food",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 100,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/gangotree.jpg",  
        "landmark": "Akurdi Railway Station",
        "veg": True,
        "otheroptions": ["Various Maharashtraian Dishes"]
    },
    {
        "name": "Chicken Biryani",
        "location": "https://maps.app.goo.gl/FQVJg86cRFfzmsBd6",
        "hotelname": "Gaarva Biryani",
        "type": "Biryani",
        "rating": 4.5,
        "price": 100,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/biryani.jpeg",  
        "landmark": "Gurudwara Chowk",
        "veg": False,
        "otheroptions": ["Various types of biryani"]
    },
    {
        "name": "Misal Paav",
        "location": "https://maps.app.goo.gl/FQVJg86cRFfzmsBd6",
        "hotelname": "CSK",
        "type": "Misal",
        "rating": 4.5,
        "price": 70,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/csk.jpg",  
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Foods"]
    },
    {
        "name": "Noodles",
        "location": "https://maps.app.goo.gl/FQVJg86cRFfzmsBd6",
        "hotelname": "CSK",
        "type": "Misal",
        "rating": 4.5,
        "price": 70,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/csk.jpg",  
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Foods"]
    },
    
    {   "name": "Medu Vada",
        "location": "https://maps.app.goo.gl/a3aBg76Sk9DcNDQX8",
        "hotelname": "CSK",
        "type": "South Indian",
        "rating": 4.5,
        "price": 40,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/csk.jpg",  
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Foods South Indian"]
    },

    {   "name": "Idli",
        "location": "https://maps.app.goo.gl/a3aBg76Sk9DcNDQX8",
        "hotelname": "CSK",
        "type": "South Indian",
        "rating": 4.5,
        "price": 50,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/csk.jpg",  
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Foods South Indian"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/a3aBg76Sk9DcNDQX8",
        "hotelname": "CSK",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/csk.jpg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/TPPF3pjZWyantBgj9",
        "hotelname": "Morya",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/morya.jpeg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    }, 

    {   "name": "Vada Pav",
        "location": "https://maps.app.goo.gl/TPPF3pjZWyantBgj9",
        "hotelname": "Morya",
        "type": "Vada pav",
        "rating": 4.5,
        "price": 15,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/morya.jpeg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    },

    {   "name": "Tea",
        "location": "https://maps.app.goo.gl/TPPF3pjZWyantBgj9",
        "hotelname": "Morya",
        "type": "Tea",
        "rating": 4.5,
        "price": 12,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/morya.jpeg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of cold drinks"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/TPPF3pjZWyantBgj9",
        "hotelname": "Morya",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/morya.jpeg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/YEt2vjiKYGBupirp7",
        "hotelname": "Savi",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/savi.jpg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    },

    {   "name": "Burger",
        "location": "https://maps.app.goo.gl/NruKLr7133EWzg198",
        "hotelname": "SK's Crown Burger ",
        "type": "Burger",
        "rating": 4.5,
        "price": 110,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/sk.jpg", 
        "landmark": "PCCOE",
        "veg": True,
        "otheroptions": ["Various types of Burgers"]
    },

    {   "name": "Chicken Burger",
        "location": "https://maps.app.goo.gl/NruKLr7133EWzg198",
        "hotelname": "SK's Crown Burger ",
        "type": "Burger",
        "rating": 4.5,
        "price": 160,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/sk.jpg", 
        "landmark": "PCCOE",
        "veg": False,
        "otheroptions": ["Various types of Burgers"]
    },

    {   "name": "Samosa",
        "location": "https://maps.app.goo.gl/zcpWBmA3ZsXL3obP6",
        "hotelname": "City Samosa ",
        "type": "Samosa",
        "rating": 4.5,
        "price": 18,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/city.jpg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of Samosa"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/DkiynykftnL1NF9F9",
        "hotelname": "Shree Mahalaxmi Mess",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 80,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/laxmi.jpg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    },

    {   "name": "Biryani ",
        "location": "https://maps.app.goo.gl/rrZGshE7wo3DYw8p8",
        "hotelname": "Hyderabadi Jayka Biryani",
        "type": "Biryani",
        "rating": 4.5,
        "price": 140,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/biryani.jpeg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of Biryani"]
    },

    {   "name": "Chicken Biryani ",
        "location": "https://maps.app.goo.gl/rrZGshE7wo3DYw8p8",
        "hotelname": "Hyderabadi Jayka Biryani",
        "type": "Biryani",
        "rating": 4.5,
        "price": 140,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/biryani.jpeg", 
        "landmark": "Dharmaraj Chowk",
        "veg": False,
        "otheroptions": ["Various types of Biryani"]
    },

    {   "name": " Chicken Roll",
        "location": "https://maps.app.goo.gl/sFXyXxRsZRdy7uaJ9",
        "hotelname": "Shrirang Rock & Roll",
        "type": "Role",
        "rating": 4.5,
        "price": 20,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/chickenroll.jpeg", 
        "landmark": "Dharmaraj Chowk",
        "veg": False,
        "otheroptions": ["Various types of rolls"]
    },

    {   "name": "Thick Coffee",
        "location": "https://maps.app.goo.gl/V31a23Si5ZpVGnGy5",
        "hotelname": "Coffee",
        "type": "Role",
        "rating": 4.5,
        "price": 30,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/cc.jpeg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of cold drinks"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/nuFK4TrcRJHBMyFMA",
        "hotelname": "Hotel Shreyas",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 70,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/shreyas.jpg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of Maharashtrian Foods"]
    },


    {   "name": "Dosa",
        "location": "https://maps.app.goo.gl/7LXuvSwFPuroqNPy6",
        "hotelname": "Dakshin Dosa",
        "type": "Dosa",
        "rating": 4.5,
        "price": 60,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/dosa.jpeg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of South Indian Food"]
    },

    {   "name": "Misal",
        "location": "https://maps.app.goo.gl/xdAqN2A8NQ1SX7Cz6",
        "hotelname": "Shindeshahi Amruttulya",
        "type": "Misal",
        "rating": 4.5,
        "price": 60,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/shindeshahi.jpg", 
        "landmark": "Dharmaraj Chowk",
        "veg": True,
        "otheroptions": ["Various types of Food"]
    },

    {   "name": "Chicken Biryani ",
        "location": "https://maps.app.goo.gl/WbngdNj7pRXwiofr7",
        "hotelname": " Laziz Biryani",
        "type": "Biryani",
        "rating": 4.5,
        "price": 120,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/biryani.jpeg", 
        "landmark": "Dharmaraj Chowk",
        "veg": False,
        "otheroptions": ["Various types of Biryani"]
    },

    {   "name": "Fruit Juice",
        "location": "https://maps.app.goo.gl/WbngdNj7pRXwiofr7",
        "hotelname": "Shivam Juice",
        "type": "Juice",
        "rating": 4.5,
        "price": 50,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/juice.jpg", 
        "landmark": "Maa Vaishino Devi Dham",
        "veg": True,
        "otheroptions": ["Various types of Juice"]
    },

    {   "name": "Dal Bati",
        "location": "https://maps.app.goo.gl/1NN9Gs1N22pF5tZK7",
        "hotelname": "Sugam Pure Veg Dining",
        "type": "Dal Bati",
        "rating": 4.5,
        "price": 90,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/dalbati.jpeg", 
        "landmark": "Maa Vaishino Devi Dham",
        "veg": True,
        "otheroptions": ["Various types of rajasthani Food"]
    },

    {   "name": "Rice Plate",
        "location": "https://maps.app.goo.gl/1NN9Gs1N22pF5tZK7 ",
        "hotelname": "Sarovar",
        "type": "Rice Plate",
        "rating": 4.5,
        "price": 60,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/riceplate.jpeg", 
        "landmark": "Maa Vaishino Devi Dham",
        "veg": True,
        "otheroptions": ["Various types of Indian Food"]
    },

    {   "name": "Vada Pav",
        "location": "https://maps.app.goo.gl/xufVJebaDxTq44jg6",
        "hotelname": "Talbidkar vadawale",
        "type": "Vada Pav",
        "rating": 4.5,
        "price": 18,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/wadapaav.jpeg", 
        "landmark": "Maa Vaishino Devi Dham",
        "veg": True,
        "otheroptions": ["Various types of Vada Pav"]
    },

    {   "name": "Vada Pav",
        "location": "https://maps.app.goo.gl/t3yaXpqNzf2jpPSdA",
        "hotelname": "Kokate vada pav",
        "type": "Vada Pav",
        "rating": 4.5,
        "price": 18,
        "quantity": 1,
        "time": "All Day",
        "imageurl": "static/images/kokate.jpg", 
        "landmark": "Near Akurdi Raiway station",
        "veg": True,
        "otheroptions": ["Various types of Vada Pav"]
    }
]

# Insert food data into MongoDB
food_collection.insert_many(food_data)
print("Food data inserted successfully!")

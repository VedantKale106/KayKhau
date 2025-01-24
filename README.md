# KayKhau - Your Food Suggester

KayKhau is a Flask-based web application that allows users to explore food options, filter based on preferences, view the hotels and their delicacies. It connects to a MongoDB database for storing food, user, and feedback information.

## Features

- **User Authentication**: Secure login and registration (Actually I have not added encryption, no worries, I am not taking any sensitive information).
- **Food Recommendations**: Randomized food suggestions on the homepage.
- **Search and Filter**: Search for dishes by name or filter by type, landmark, price, and rating.
- **Food Details**: Detailed page for each dish with its information.
- **Hotel Details**: Detailed page for each hotel and the dishes which the hotel contains.
- **Feedback System**: Users can submit feedback for dishes.
- **Responsive Design**: Mobile-friendly UI.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Frontend**: HTML, CSS (custom styling)
- **Deployment**: Vercel

## Installation

1. **Clone the repository**:
   git clone https://github.com/your-repo/kaykhau.git
   cd kaykhau
   

2. **Install dependencies**:
   pip install -r requirements.txt
   

3. **Configure the environment variables**:
   Create a \`.env\` file in the project directory with the following content:
   SECRET_KEY=your_secret_key
   MONGO_URI=your_mongo_connection_string
   

4. **Initialize the database**:
   python mongo.py
   

5. **Run the application**:
   python app.py

6. **Open your browser**:
   Navigate to \`http://127.0.0.1:5000\'

## Folder Structure

\`\`\`plaintext
.
├── app.py                  # Main application file\n
├── mongo.py                # MongoDB initialization and dummy data
├── build.sh                # Build script for deployment
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel configuration
├── templates/              # HTML templates
│   ├── all_foods.html      # Food listing page
│   ├── filter.html         # Food filter page
│   ├── feedback.html       # Feedback form
│   ├── food_details.html   # Food details page
│   └── homepage.html       # Homepage
└── static/                 # Static assets (images, CSS, etc.)
\`\`\`

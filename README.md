# 🔐 Flask Authentication App

A Flask web application that implements user authentication using `Flask-Login`, `Werkzeug` for secure password hashing, and SQLite as the database (via SQLAlchemy). Users can register, log in, and log out securely.

## 🚀 Features

- User Registration (Sign-Up)
- Secure Login with Password Hashing
- Logout Functionality
- Flash Message Alerts for Validation
- Session Management with Flask-Login
- Blueprint Structure for Modular Design

## 📁 Project Structure

/your_project
│
├── app/
│ ├── init.py # Initializes Flask app and DB
│ ├── models.py # SQLAlchemy User model
│ ├── auth.py # Auth blueprint (this file)
│ └── views.py # Other views (e.g., home page)
│
├── templates/
│ ├── login.html
│ ├── sign_up.html
│ └── home.html
│
├── static/ # CSS, JS, images
│
├── main.py # Entry point
└── requirements.txt

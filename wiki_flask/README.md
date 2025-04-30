# wiki_flask

## Overview
This project is a Flask web application that provides user authentication features, including registration, login, and logout functionalities. It utilizes a database to store user information securely.

## Project Structure
```
wiki_flask
├── app
│   ├── __init__.py          # Initializes the Flask application and sets up the context
│   ├── models.py            # Defines the data models, including the User model
│   ├── routes
│   │   ├── __init__.py      # Initializes the routes and registers blueprints
│   │   └── auth.py          # Contains authentication routes for registration, login, and logout
│   ├── static               # Directory for static files (CSS, JavaScript, images)
│   └── templates            # Directory for HTML templates
│       ├── base.html        # Base template for the application
│       ├── login.html       # HTML for the login page
│       └── register.html    # HTML for the registration page
├── config.py                # Configuration settings for the Flask application
├── requirements.txt         # Lists dependencies required for the project
└── README.md                # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd wiki_flask
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure the application**:
   Update `config.py` with your database URI and secret keys.

5. **Run the application**:
   ```
   flask run
   ```

## Usage
- Navigate to `/register` to create a new account.
- Navigate to `/login` to access your account.
- Use the logout option to exit your session.

## Features
- User registration with password hashing.
- User login with password verification.
- Logout functionality.
- Basic error handling and user feedback.

## License
This project is licensed under the MIT License.
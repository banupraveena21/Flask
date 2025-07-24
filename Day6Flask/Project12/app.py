'''
12. Library Book Borrowing System 
 Features: 
 Users can log in and borrow books. 
 Use session to track recently borrowed books. 
 Admin sees list of all borrowed books (optional). 
 Login-required routes and hashed credentials.
'''

from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app, login_manager)

if __name__ == '__main__':
    app.run(debug=True)

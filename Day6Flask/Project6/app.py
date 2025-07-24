'''
6. Movie Review App 
 Features: 
 Registered users can submit reviews (rating + comment). 
 Use @login_required for review routes. 
 Flash messages for login, review submission, and logout. 
 Protect “Add Review” button for only logged-in users. 
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

'''
7. Bug Reporting System 
 Features: 
 Authenticated users can submit bug reports. 
 Use session to store last submitted bug title. 
 View only your submitted bugs. 
 Redirect to /login if not logged in.  give style.css 
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

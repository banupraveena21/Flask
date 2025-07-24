'''
1. Personal Task Manager 
 Features: 
 Users register/login to manage their own tasks. 
 Tasks include title, due date, and completion status. 
 Use @login_required to ensure only logged-in users can CRUD their tasks. 
 Flash success/error messages. 
 Hash passwords and restrict password length < 8. 
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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

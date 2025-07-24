'''
5. Online Quiz Platform (User Dashboard) 
 Features: 
 Users register and take quizzes (each session tied to user). 
 Store score in DB; show only their score in the dashboard. 
 Only logged-in users can access /quiz and /results. 
 Flash messages on login/logout and completion. 
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

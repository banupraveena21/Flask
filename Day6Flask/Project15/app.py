'''
15. Customer Feedback System 
 Features: 
 Only logged-in users can submit feedback. 
 Admin view for all feedback (if role management is added). 
 Flash: “Thank you for your feedback!” 
 Hash and verify passwords during login. 
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

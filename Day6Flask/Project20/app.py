'''
20. Admin-Only Dashboard (User Auth) 
 Features: 
 Allow only admin users to access certain routes. 
 Use Flask-Login to check for admin flag. 
 Hash passwords, verify credentials on login. 
 Flash message: “Admin only access!” 
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


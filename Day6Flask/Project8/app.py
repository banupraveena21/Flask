'''
8. Simple E-Commerce Admin Panel 
 Features: 
 Admin login with hashed password (admin@example.com). 
 Admin can add/edit/delete products (CRUD protected). 
 Use Flask-Login to differentiate between admin/user roles. 
 Flash messages for product actions.
'''

from flask import Flask
from flask_login import LoginManager
from models import db, Admin
from config import Config
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()
    # Create default admin if not exists
    if not Admin.query.filter_by(email="admin@example.com").first():
        admin = Admin(email="admin@example.com")
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()

register_routes(app, login_manager)

if __name__ == '__main__':
    app.run(debug=True)

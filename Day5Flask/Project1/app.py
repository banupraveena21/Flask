'''
1. User Management System 
 Requirements: 
 Database: SQLite 
 Model: User(id, name, email, password, joined_on) 
 Operations: 
o Create a user via form 
o Read list of all users 
o Update user details 
 Delete user record 
 Use SQLAlchemy + render_template() for listing 
 Flash messages after each operation
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)



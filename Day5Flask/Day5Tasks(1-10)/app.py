# 1. Setting Up SQLite / MySQL / PostgreSQL with Flask  
'''
1. Install Flask-SQLAlchemy using pip install flask-sqlalchemy 
2. Set up a Flask app with SQLite and test DB connection 
3. Change the connection string to MySQL and connect (e.g., 
mysql+pymysql://user:pass@localhost/db) 
4. Set up PostgreSQL with psycopg2 and test database connection 
5. Create a reusable config.py for DB URI settings 
6. Use environment variables for database URIs 
7. Create a db = SQLAlchemy(app) instance in your main app 
8. Create and initialize the database with db.create_all() 
9. Handle database connection errors gracefully with try-except 
10. Switch between development and production DB configurations 
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

from routes import *


if __name__ == "__main__":
    app.run(debug=True)


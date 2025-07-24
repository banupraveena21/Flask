'''
2. Simple Blog System 
 Requirements: 
 Model: Post(id, title, content, author, created_at) 
 Add new blog posts via a form 
 View all blog posts (most recent first) 
 Edit and delete posts 
 Use SQLite or PostgreSQL 
 Show flash messages on create/update/delete
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes import *

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)

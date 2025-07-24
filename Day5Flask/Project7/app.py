'''
7. Book Inventory Tracker 
 Requirements: 
 Model: Book(id, title, author, quantity, published_year) 
 Add books to the inventory 
 Update quantity if stock changes 
 Delete books if discontinued 
 List books sorted by published year 
'''

from flask import Flask
from config import Config
from models import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

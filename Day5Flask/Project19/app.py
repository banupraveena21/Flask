'''
19. Simple Inventory Management 
 Requirements: 
 Model: Item(id, name, quantity, updated_on) 
 Add new stock items 
 Update quantity and timestamp 
 Delete items when zero stock 
 Use PostgreSQL or MySQL 
'''

# app.py

from flask import Flask
from config import Config
from models import db
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)

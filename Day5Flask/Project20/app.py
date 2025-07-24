'''
20. Feedback Review Panel 
 Requirements: 
 Model: Feedback(id, user_name, rating, comment) 
 Submit ratings (1–5 stars) and comments 
 Admin can view, update, or delete feedback 
 Use validators.NumberRange(1, 5) for rating
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

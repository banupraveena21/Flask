'''
13. Expense Tracker 
 Requirements: 
 Model: Expense(id, name, amount, category, date) 
 Add, view, update, and delete expenses 
 Display expenses grouped by category or date 
 Use MySQL or SQLite exactly like above program
'''

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

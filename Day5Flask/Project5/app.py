'''
5. Task Manager (To-Do List) 
 Requirements: 
 Model: Task(id, title, is_done, due_date) 
 Add new tasks 
 Mark tasks as done/undone (update) 
 Delete completed tasks 
 View tasks ordered by due date give exactly like above task
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

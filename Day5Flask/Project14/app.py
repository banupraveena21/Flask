'''
14. Employee Management System 
 Requirements: 
 Model: Employee(id, name, position, department, salary) 
 Perform full CRUD on employees 
 Add filtering by department 
 Flash confirmation messages after update/delete 
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

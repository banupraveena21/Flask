'''
3. Product Catalog Manager 
 Requirements: 
 Model: Product(id, name, price, in_stock, description) 
 Admin can: 
o Add products via form 
o View all products in a table 
o Edit and delete any product 
 In-stock products shown separately 
 Use MySQL connection string and configuration
'''

from flask import Flask
from config import Config
from models import db
import routes  

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

# Using Jinja2: {{ variables }}, {% for %}, {% if %}     
# 4. Create a route /scores and pass a list of numbers, display them in a list in HTML. 
# 5. Inside {% for %}, use loop.index to show the serial number of each item. 
# 6. Use nested {% if %} inside {% for %} to mark certain values (e.g., highlight scores > 80). 
# 7. Use {% else %} to display a message when a passed list is empty. 
# 12. Render a Bootstrap-styled card for each product in a product list. 

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    username = "Mahesh"
    tech_stack = ["Python", "Flask", "Jinja"]
    logged_in = True
    current_date = datetime.now()
    name = "mahesh"
    role = "admin"
    welcome_html = "<strong>Hello, <em>Mahesh</em></strong>!"
    description = "This is a very long description that should be shortened in the template using slicing."

    user_data = {
        "email": "mahesh@gmail.com",
        "location": "Tenkasi",
        "joined": "2021"
    }

    return render_template(
        'home.html',
        username=username,
        tech_stack=tech_stack,
        logged_in=logged_in,
        current_date=current_date,
        name=name,
        role=role,
        welcome_html=welcome_html,
        description=description,
        user_data=user_data
    )

@app.route('/scores')
def scores():
    score_list = [45, 67, 89, 92, 73]
    return render_template('scores.html', scores=score_list)

@app.route('/products')
def products():
    products = [
        {"name": "Laptop", "price": 1000, "desc": "High performance laptop"},
        {"name": "Phone", "price": 500, "desc": "Latest model smartphone"},
        {"name": "Tablet", "price": 300, "desc": "Lightweight tablet"}
    ]
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
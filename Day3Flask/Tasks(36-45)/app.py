# Sending data from Flask to HTML using render_template()  
# 1. Create a route /user/<name> and send name to a template. 
# 2. Pass a list of courses from Flask to HTML and display using a loop. 
# 3. Send a boolean flag is_logged_in and show login/logout button conditionally. 
# 4. Pass a dictionary (e.g., user profile) and access fields in HTML. 
# 5. Send current date and time from Flask to HTML. 
# 6. Create a news list and pass it to the template as news_items. 
# 7. Pass multiple variables (name, age, city) and display them as a profile card. 
# 8. Use render_template() to send a dynamic title to each page. 
# 9. Loop through list of dictionaries (products with name and price) and render as cards. 
# 10. Add logic in Flask to compute something (like tax) and pass it to template for display.


from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 1. /user/<name>
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, title="User Page")

# 2. List of courses
@app.route('/courses')
def courses():
    course_list = ["Python", "Flask", "Jinja2", "SQL", "JavaScript"]
    return render_template('courses.html', courses=course_list, title="Courses")

# 3. Boolean flag for login
@app.route('/profile')
def profile():
    is_logged_in = True
    user = {
        'name': 'banu',
        'email': 'banu@gmail.com',
        'age': 34,
        'city': 'Hosur'
    }
    current_time = datetime.now()
    return render_template(
        'profile.html',
        user=user,
        is_logged_in=is_logged_in,
        current_time=current_time,
        title="User Profile"
    )

# 6. News list
@app.route('/news')
def news():
    news_items = [
        "Flask 2.0 Released!",
        "Python 3.12 Beta Available",
        "Jinja2 Template Tips You Didn't Know"
    ]
    return render_template('news.html', news_items=news_items, title="Latest News")

# 7. Multiple variables - Profile Card
@app.route('/card')
def profile_card():
    return render_template('profile.html',
        user={'name': 'banu', 'age': 34, 'city': 'Hosur'},
        is_logged_in=True,
        current_time=datetime.now(),
        title="Banu's Card"
    )

# 9. Products (list of dictionaries)
@app.route('/products')
def products():
    items = [
        {'name': 'Laptop', 'price': 1000},
        {'name': 'Mouse', 'price': 25},
        {'name': 'Monitor', 'price': 200}
    ]
    return render_template('products.html', products=items, title="Product Catalog")

# 10. Tax Calculation Example
@app.route('/tax')
def tax():
    price = 1200
    tax_rate = 0.1
    tax_amount = price * tax_rate
    total = price + tax_amount
    return render_template('products.html',
                           products=[{'name': 'Laptop', 'price': price}],
                           tax=tax_amount,
                           total=total,
                           title="Tax Example")

if __name__ == '__main__':
    app.run(debug=True)

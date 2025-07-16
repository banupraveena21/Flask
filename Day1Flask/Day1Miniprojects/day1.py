# Section 2: Installing Flask (10 Tasks)
# 11. Create a virtual environment and activate it.
# Python -m venv .venv

# To activate
# .venv\Scripts\activate


# 12. Install Flask using pip and verify the installation.
# pip install flask


# 13. Check the installed Flask version and print it.
# flask --version

# 14. Create a requirements.txt file with Flask listed.
# pip freeze > requiremnents.txt


# 15. Install Flask from a requirements.txt file in a new environment.
# pip install -r requirements.txt

#16. Upgrade Flask to the latest version using pip.
# pip install --upgrade Flask

# 17. Uninstall Flask and reinstall it.
# pip uninstall Flask
# pip install Flask

# 18. Explore and list down any 5 Flask-related packages on PyPI.
# Flask-RESTful — for building REST APIs
# Flask-SQLAlchemy — SQLAlchemy support
# Flask-WTF — WTForms integration
# Flask-Login — user session management
# Flask-Migrate — database migrations


# 19. Use pip freeze to generate a complete environment dependency list.
# pip freeze > requirements.tx

# 20. Create a bash script to set up a virtual environment and install Flask automatically.
'''
#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install Flask

echo "Virtual environment created and Flask installed."

chmod +x setup.sh

./setup.sh
'''



#Section 3: Creating your First Flask App (10 Tasks)
#21. Create a new file named app.py.
# app.py

#28. Add comments to each section of the app.py explaining what it does.
#22. Import Flask correctly in your script.
from flask import Flask  # Importing Flask

#23. Create a basic Flask application instance.
app = Flask(__name__)       # Create a Flask app instance

#24. Add a basic home route / that returns "Hello, Flask!".
# 35. Add a print statement and observe console output on page refresh.
@app.route("/")
def home():
    print("Home page was accessed")
    return "Hello, Flask! This is Home Page."          # Response for root URL
    
#26. Add another route /about returning "This is the about page".
@app.route("/about")
def about():
    return "This is the about page"


#30. Try adding a wrong syntax and observe Flask's debug error page.
@app.route("/error")
def error():
    return "This will crash"


#Section 5: Understanding route() and @app.route() (5 Tasks)
# 41. Define a route /hello that returns a welcome message.
@app.route("/hello")
def hello():
    return "Welcome to the Flask App!"

# 42. Add a route /user/<username> and return a dynamic message with the username.
@app.route("/user/<username>")
def show_user(username):
    return f"Hello, {username.capitalize()}!"

# 43. Add multiple routes pointing to the same function.
@app.route("/")
@app.route("/home")
def homepage():
    return "This is the homepage!"

# 44. Add different HTTP methods (GET, POST) in a route and print the method used.
@app.route("/method-check", methods=["GET", "POST"])
def method_check():
    return f"Request method used:"

# 45. Explain what happens when you define two functions with the same route.
@app.route("/duplicate")
def first():
    return "This is the first function"

@app.route("/duplicate")
def second():
    return "This is the second function"





# Section 4: Running the Flask Development Server (10 Tasks)
# 31. Run the Flask app using flask run command with FLASK_APP=app.py.
'''
set FLASK_APP=app.py
flask run
'''

# 32. Use the --debug flag while running the server and observe the behavior.
'''
flask run --debug
'''

# 33. Change the port from the default (5000) to 8000 and access it.
'''
flask run --port=8000
'''

# 34. Enable auto-reloading using debug mode and test it.
'''
flask run --debug
'''

# 36. Run the Flask app in production mode (not using debug).
'''
flask run --no-debugger --no-reload
'''

# 37. Explain the difference between running with python app.py and flask run.
'''
python app.py	                            flask run
Runs the script directly	                Uses Flask CLI
You control app.run()	                    CLI manages server, host, port
Good for quick testing	                    More flexible, better in dev setup
'''

# 38. Set environment variables using .env file for Flask app and debug mode.
'''
FLASK_APP=app.py
FLASK_DEBUG=1

flask run
'''

# 39. Access your app from another device in the same network using host 0.0.0.0.
'''
flask run --host=0.0.0.0 --port=8000
'''

#40. Write a note on common issues faced while running the server (port conflicts, missing env vars).
'''
Problem	                                Reason	                                    Fix
Port already in use	         Another process using the same port	                Use a different port: flask run --port=8001
ModuleNotFoundError	         Flask not installed in current venv	                Activate correct environment
.env not loaded	             Not in root dir, or incorrect syntax	                Place .env in the app folder
FLASK_APP not set	         Flask can't find your app	                            Set manually or use .env
External access fails	     Not using --host=0.0.0.0	                            Add --host=0.0.0.0 flag
'''



# Section 6: Returning Simple HTML Responses (5 Tasks)
# 46. Return a basic HTML structure from a route.
@app.route("/basic")
def basic_html():
    return "<html><body><h1>Hello from Flask!</h1></body></html>"

# 47. Add inline CSS styling to the returned HTML.
@app.route("/styled")
def styled():
    return """
    <html>
        <body>
            <h1 style="color:blue; text-align:center;">Styled Flask Page</h1>
            <p style="font-size:18px;">This has inline CSS!</p>
        </body>
    </html>
    """

# 48. Return a multiline HTML string from a Python triple-quoted string.
@app.route("/multiline")
def multiline():
    return """
    <html>
        <head><title>Multi-line Example</title></head>
        <body>
            <h2>Welcome</h2>
            <p>This is written using triple-quoted strings in Python.</p>
        </body>
    </html>
    """

# 49. Return an unordered list with 3 items from an HTML response.
@app.route("/list")
def show_list():
    return """
    <h2>My Favorite Fruits</h2>
    <ul>
        <li>Apple</li>
        <li>Mango</li>
        <li>Banana</li>
    </ul>
    """

# 50. Use basic HTML tags like <h1>, <p>, <br>, <hr> and explain their output.
@app.route("/tags")
def tags_demo():
    return """
    <h1>HTML Tags Demo</h1>
    <p>This is a paragraph.</p>
    <br>
    <p>Line break above ↑</p>
    <hr>
    <p>Horizontal line above ↑</p>
    """


#25. Run the app using python app.py and open it in the browser.
#27. Print something in the console when the server starts.
#29. Create an app.run(debug=True) statement and explain the debug mode.

if __name__ == "__main__":
    print("Starting Server...")         # Console message
    app.run(debug=True)                 # Enable debug mode for development


# Basic User Tracker
'''
Requirements:
• /user/<name> returns "Welcome, [name]!".
• /user/<name>/location/<city> returns “Hi [name], how is [city]?”.
• Add console print when each route is accessed.
• Demonstrate how Flask captures URL parameters.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/user/<string:name>")
def greet_user(name):
    print(f"[INFO] /user/{name} accessed")  
    return f"<h2>Welcome, {name}!</h2>"

@app.route("/user/<string:name>/location/<string:city>")
def user_location(name, city):
    print(f"[INFO] /user/{name}/location/{city} accessed")  
    return f"<h3>Hi {name}, how is {city}?</h3>"

if __name__ == "__main__":
    app.run(debug=True)

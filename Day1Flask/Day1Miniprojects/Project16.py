# Day/Night Greeter
'''
Requirements:
• /greet/<hour> returns "Good Morning", "Afternoon", or "Night" based on hour.
• Add route /greet/info showing valid hours.
• Demonstrate restarting server with debug mode to reflect code change.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/greet/<int:hour>")
def greet(hour):
    if hour < 0 or hour > 23:
        return "<p style='color:red;'>Invalid hour! Please enter 0–23.</p>"

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Night"

    return f"""
    <h2 style="color:darkblue;">{greeting}!</h2>
    <p>The hour you entered: <strong>{hour}</strong></p>
    """

@app.route("/greet/info")
def greet_info():
    return """
    <h3>Greet Info</h3>
    <p>Enter the hour (0–23) to get a time-based greeting.</p>
    <p><strong>Example:</strong> /greet/10 for "Good Morning"</p>
    <hr>
    """

if __name__ == "__main__":
    app.run(debug=True)
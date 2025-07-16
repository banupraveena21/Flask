# Online Business Hours Page
'''
Requirements:
• / shows “We are open!” or “Closed” based on server time.
• /contact returns HTML with email and phone number.
• Use app.run(debug=True) and explain debug mode errors.
• Show inline HTML formatting with <b>, <p>, <hr> etc.
'''

from flask import Flask
from datetime import datetime

app = Flask(__name__)


def is_open():
    now = datetime.now()
    return 9 <= now.hour < 17  

@app.route("/")
def home():
    if is_open():
        status = "<h1><b>We are open!</b></h1>"
    else:
        status = "<b>Sorry, we are closed.</b>"
    return f"<p>{status}</p><hr><p>Business hours: 9 AM to 5 PM</p>"

@app.route("/contact")
def contact():
    return """
    <h2>Contact Us</h2>
    <p><b>Email:</b> banu@gmail.com</p>
    <p><b>Phone:</b> +91 85310- 83086</p>
    <hr>
    <p>We usually respond within 24 hours.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
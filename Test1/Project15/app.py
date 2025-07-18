'''
15. Time-Based Greeting App
•	Route /greet
•	Query param: ?hour=9
•	Show greeting (Morning, Afternoon, Night) using {% if %}
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet')
def greet():
    hour = request.args.get('hour', type=int)
    # Default to None if invalid
    if hour is None or hour < 0 or hour > 23:
        hour = -1  # invalid flag

    return render_template('greet.html', hour=hour)

if __name__ == '__main__':
    app.run(debug=True)

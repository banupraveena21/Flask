# 12. Custom Greeting Generator
'''
Requirements:
- /greet: GET query string like ?name=Arivu&time=morning
- /custom-greet/<name>: Dynamic greeting
- Show form to enter name and time, POST to /submit-greet
- Redirect to /greet-result after submission
'''


from flask import Flask, request, redirect, url_for

app = Flask(__name__)


last_greeting = {}


@app.route('/greet')
def greet_query():
    name = request.args.get('name')
    time = request.args.get('time')
    if not name or not time:
        return "<p>Please provide both name and time as query parameters (e.g. /greet?name=Arivu&time=morning).</p>"

    return f"<h3>Good {time.title()}, {name.title()}!</h3>"


@app.route('/custom-greet/<name>')
def custom_greet(name):
    return f"<h3>Hello {name.title()}! This is your custom greeting 🎉</h3>"


@app.route('/submit-greet', methods=['GET', 'POST'])
def submit_greet():
    global last_greeting

    if request.method == 'POST':
        name = request.form.get('name')
        time = request.form.get('time')
        last_greeting = {'name': name, 'time': time}
        return redirect(url_for('greet_result'))

    return '''
    <h2>Custom Greeting Form</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Time of Day:
        <select name="time" required>
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
            <option value="night">Night</option>
        </select><br><br>
        <input type="submit" value="Generate Greeting">
    </form>
    '''


@app.route('/greet-result')
def greet_result():
    name = last_greeting.get('name')
    time = last_greeting.get('time')
    if not name or not time:
        return redirect(url_for('submit_greet'))

    return f"<h3>🌞 Good {time.title()}, {name.title()}! Have a wonderful day!</h3>"


if __name__ == '__main__':
    app.run(debug=True)
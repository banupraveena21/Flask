'''
14. Simple Login Page (No Auth)
•	Form with username and password
•	On submit, show "Welcome, {{ username }}" with message
•	Use request.form, redirect
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')  # Not used for auth here
        if username:
            return redirect(url_for('welcome', username=username))
        else:
            error = "Please enter a username."
            return render_template('login.html', error=error)
    return render_template('login.html', error=None)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    if not username:
        return redirect(url_for('login'))
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

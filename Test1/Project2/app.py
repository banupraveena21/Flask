'''
2. Greeting App
•	Dynamic route /greet/<name> that shows a welcome message
•	Query param lang=en shows greeting in different languages
•	Template uses {{ name }} and {% if %} to select language
•	Base template with nav
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/greet/<name>')
def greet(name):
    lang = request.args.get('lang', 'en')  
    return render_template('greet.html', name=name, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)

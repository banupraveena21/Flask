'''
17. Resume Formatter
•	Form inputs: name, email, experience
•	Output a resume-style HTML using submitted data
•	Render with base template
•	Use static/css/resume.css for print layout
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        experience = request.form.get('experience')
        if not (name and email and experience):
            error = "Please fill in all fields."
            return render_template('form.html', error=error, name=name, email=email, experience=experience)
        return render_template('resume.html', name=name, email=email, experience=experience)
    return render_template('form.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)

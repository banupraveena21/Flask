'''
12. Survey Voting Page
•	Route /survey (GET shows form)
•	On POST, redirect to /thank-you with vote summary
•	Result page uses {% if %} to show different messages
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        vote = request.form.get('vote')
        if vote:
            return redirect(url_for('thank_you', vote=vote))
        else:
            error = "Please select an option before submitting."
            return render_template('survey.html', error=error)
    return render_template('survey.html', error=None)

@app.route('/thank-you')
def thank_you():
    vote = request.args.get('vote')
    return render_template('thank_you.html', vote=vote)

if __name__ == '__main__':
    app.run(debug=True)


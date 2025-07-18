'''
3. Feedback Collector
•	GET shows a form to submit feedback
•	POST handles form and redirects to thank-you page
•	Use request.form and url_for() redirect
•	Display submitted feedback on a separate page with Jinja2 loop
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store feedback
feedback_data = []

@app.route('/', methods=['GET', 'POST'])
def feedback_form():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        feedback_data.append({'name': name, 'message': message})
        return redirect(url_for('thank_you'))
    return render_template('feedback_form.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/all-feedback')
def all_feedback():
    return render_template('feedback_list.html', feedback=feedback_data)

if __name__ == '__main__':
    app.run(debug=True)

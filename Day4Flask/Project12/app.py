# 12. Job Application Form 
'''
Requirements: 
 Fields: Name, Email, Resume URL, Experience (Integer) 
 Validators: Resume URL must be a valid URL, Experience ≥ 0 
 Flash confirmation message 
 Highlight field errors with red borders 
'''

from flask import Flask, render_template, request, redirect, flash, url_for
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

def is_valid_url(url):
    pattern = re.compile(
        r'^(http|https)://[^\s]+$'
    )
    return re.match(pattern, url)

@app.route('/', methods=['GET', 'POST'])
def job_application():
    errors = {}
    values = {}

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        resume_url = request.form.get('resume_url', '').strip()
        experience = request.form.get('experience', '').strip()

        # Keep entered values in case of errors
        values = {'name': name, 'email': email, 'resume_url': resume_url, 'experience': experience}

        # Validation
        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not is_valid_url(resume_url):
            errors['resume_url'] = 'Invalid Resume URL.'
        try:
            experience_val = int(experience)
            if experience_val < 0:
                errors['experience'] = 'Experience must be 0 or more.'
        except ValueError:
            errors['experience'] = 'Experience must be an integer.'

        if not errors:
            flash('Application submitted successfully!', 'success')
            return redirect(url_for('job_application'))

    return render_template('form.html', errors=errors, values=values)

if __name__ == '__main__':
    app.run(debug=True)
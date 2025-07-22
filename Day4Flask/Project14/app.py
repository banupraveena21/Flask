# 14. Customer Support Ticket 
'''
 Requirements: 
 Fields: Name, Email, Issue Category, Description 
 Description must be at least 25 characters 
 Flash ticket ID generated randomly 
 Display field-wise error messages
'''

from flask import Flask, render_template, request, redirect, flash, url_for
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

ISSUE_CATEGORIES = ['Billing', 'Technical Support', 'Account', 'Other']

def generate_ticket_id():
    return 'TCKT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

@app.route('/', methods=['GET', 'POST'])
def support_ticket():
    errors = {}
    values = {}

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        category = request.form.get('category', '')
        description = request.form.get('description', '').strip()

        values = {'name': name, 'email': email, 'category': category, 'description': description}

        
        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if category not in ISSUE_CATEGORIES:
            errors['category'] = 'Invalid category.'
        if len(description) < 25:
            errors['description'] = 'Description must be at least 25 characters.'

        if not errors:
            ticket_id = generate_ticket_id()
            flash(f'Ticket submitted successfully. Your Ticket ID is {ticket_id}', 'success')
            return redirect(url_for('support_ticket'))

    return render_template('support_form.html', errors=errors, values=values, categories=ISSUE_CATEGORIES)

if __name__ == '__main__':
    app.run(debug=True)
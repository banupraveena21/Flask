# 18. Complaint Registration 
'''
Requirements: 
 Fields: Name, Email, Complaint (TextArea), Category 
 Validators: Length(min=15) for complaint 
 Flash complaint number using random ID 
 Display all errors in a list at top 
'''

from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import random
import string

app = Flask(__name__)
app.secret_key = 'supersecretkey'

CATEGORIES = ['Billing', 'Service', 'Product', 'Other']

def generate_complaint_number():
    return 'CMP-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class ComplaintForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    category = SelectField('Category', choices=[(cat, cat) for cat in CATEGORIES], validators=[DataRequired()])
    complaint = TextAreaField('Complaint', validators=[DataRequired(), Length(min=15)])
    submit = SubmitField('Submit Complaint')

@app.route('/', methods=['GET', 'POST'])
def register_complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint_id = generate_complaint_number()
        flash(f'Complaint registered successfully. Your complaint number is {complaint_id}', 'success')
        return redirect(url_for('register_complaint'))
    return render_template('complaint_form.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
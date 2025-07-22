# 10. Leave Application Form 
'''
Requirements: 
 Fields: Name, Department, Reason, Start Date, End Date 
 Validate presence of all fields 
 If end date < start date, show error 
 Flash message with duration of leave
'''

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class LeaveForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    reason = TextAreaField('Reason for Leave', validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Apply for Leave')

@app.route('/', methods=['GET', 'POST'])
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        if form.end_date.data < form.start_date.data:
            form.end_date.errors.append("End date cannot be before start date.")
        else:
            duration = (form.end_date.data - form.start_date.data).days + 1
            flash(f"✅ Leave applied for {duration} day(s) from {form.start_date.data} to {form.end_date.data}", "success")
            return redirect(url_for('leave'))
    return render_template('leave.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

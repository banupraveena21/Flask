# 11. Appointment Booking Form 
'''
Requirements: 
 Fields: Name, Email, Date, Time, Purpose 
 Validators for email and required fields 
 Flash message confirming appointment 
 Display time/date input errors
'''

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class AppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M', validators=[DataRequired()])
    purpose = TextAreaField('Purpose', validators=[DataRequired()])
    submit = SubmitField('Book Appointment')

@app.route('/', methods=['GET', 'POST'])
def book():
    form = AppointmentForm()
    if form.validate_on_submit():
        flash(f"✅ Appointment booked for {form.date.data.strftime('%Y-%m-%d')} at {form.time.data.strftime('%H:%M')}", "success")
        return redirect(url_for('book'))
    return render_template('appointment.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

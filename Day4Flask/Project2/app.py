# 2. Newsletter Subscription 
'''
Requirements: 
 Fields: Name, Email, Frequency (SelectField) 
 Email must be valid 
 Flash “Subscribed successfully!” if form is valid 
 Display error under email field if invalid
'''

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,PasswordField
from wtforms.validators import DataRequired, Email,Length,EqualTo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

class NewsletterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    frequency = SelectField('Frequency', choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ], validators=[DataRequired()])
    submit = SubmitField('Subscribe')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.full_name.data}!", "success")
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    form = NewsletterForm()
    if form.validate_on_submit():
        flash("Subscribed successfully!", "success")
        return redirect(url_for('subscribe'))
    return render_template('subscribe.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# 3. Feedback Collection Form 
'''
Requirements: 
 Fields: Name, Email (optional), Message 
 Validators: Message is required and must be at least 10 characters 
 Show flash message on success and style it 
 Display all field errors if form submission fails
'''

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

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


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[Optional()])
    email = StringField('Email', validators=[Optional(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Feedback')


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

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash("Feedback submitted successfully!", "success")
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


# 1. User Registration Form 
''' 
Requirements: 
 Fields: Full Name, Email, Password, Confirm Password 
 Validators: DataRequired, Email, Length(min=6), EqualTo 
 On successful registration, flash a welcome message 
 Highlight all invalid fields with error messages
'''

from flask import Flask, render_template, redirect, url_for, flash,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.full_name.data}!", 'success')
        return redirect(url_for('success', name=form.full_name.data))
    return render_template('register.html', form=form)

@app.route('/success')
def success():
    name = request.args.get('name', 'User')
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

# 4. Login Form (with Dummy Auth) 
'''
Requirements: 
 Fields: Email, Password 
 Validate email format and password length 
 If credentials match dummy values, flash "Login successful" 
 Else, flash "Invalid credentials" and show errors 
'''

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'  


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "banu@gmail.com" and form.password.data == "banu123":
            flash("Login successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid credentials", "error")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# 20. Gym Membership Signup 
'''
Requirements: 
 Fields: Name, Age, Email, Plan (Monthly, Yearly), Accept Terms 
 Age ≥ 16, Terms (BooleanField) must be checked 
 Flash “Welcome to our gym, [name]” 
 Show required-field errors in template 
'''

from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, InputRequired

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class GymSignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=16, message="You must be at least 16 years old.")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    plan = SelectField('Plan', choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], validators=[DataRequired()])
    accept_terms = BooleanField('I accept the Terms and Conditions', validators=[InputRequired(message='You must accept the terms.')])
    submit = SubmitField('Join Now')

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = GymSignupForm()
    if form.validate_on_submit():
        flash(f"Welcome to our gym, {form.name.data}!", 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
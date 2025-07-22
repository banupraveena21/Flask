# 19. Donation Form 
'''
Requirements: 
 Fields: Name, Email, Amount (IntegerField), Cause (Select) 
 Amount must be ≥ 10 
 Flash amount and cause selected 
 Show form field error messages in red
'''

from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'secretkey'

CAUSES = ['Education', 'Health', 'Environment', 'Animal Welfare']

class DonationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    amount = IntegerField('Amount ($)', validators=[DataRequired(), NumberRange(min=10, message="Minimum donation is $10")])
    cause = SelectField('Cause', choices=[(c, c) for c in CAUSES], validators=[DataRequired()])
    submit = SubmitField('Donate')

@app.route('/', methods=['GET', 'POST'])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        flash(f'Thanks for donating ${form.amount.data} to {form.cause.data}!', 'success')
        return redirect(url_for('donate'))
    return render_template('donate.html', form=form)

if __name__=='__main__':
    app.run(debug=True)

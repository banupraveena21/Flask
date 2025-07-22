# 8. Product Review Submission 
''' 
Requirements: 
 Fields: Name, Email, Rating (1–5), Review Message 
 Rating required with range validator, Email validated 
 Flash thank-you message and style it with success class 
 Show errors using form.field.errors
'''

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  

class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    rating = IntegerField('Rating (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5)])
    message = TextAreaField('Review Message', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

@app.route('/', methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash("✅ Thank you for your review!", "success")
        return redirect(url_for('review'))
    return render_template('review.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

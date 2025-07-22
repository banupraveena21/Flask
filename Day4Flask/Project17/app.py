# 17. Password Reset Form 
'''
Requirements: 
 Fields: Email, New Password, Confirm Password 
 Email and passwords required 
 Use EqualTo for confirm password 
 Flash message and show field errors
'''


from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('new_password', message='Passwords must match')
    ])
    submit = SubmitField('Reset Password')

@app.route('/', methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash('Password reset successful!', 'success')
        return redirect(url_for('reset_password'))
    return render_template('reset_form.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
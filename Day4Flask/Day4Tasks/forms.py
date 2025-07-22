# 1. Handling User Input Using Flask-WTF  
#1. Create a form with fields: name, email, and message 



from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, TextAreaField, SubmitField,
    RadioField, SelectField, BooleanField, IntegerField, DateField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, NumberRange,
    Optional, Regexp, ValidationError
)

def block_test_domain(form, field):
    if field.data.endswith('@test.com'):
        raise ValidationError("Emails from test.com are not allowed.")

class UserForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Name is required"),
        Length(min=3, message="Name must be at least 3 characters"),
        Regexp(r'^[A-Za-z ]*$', message="Only alphabets allowed")
    ])
    email = StringField("Email", validators=[
        DataRequired(), Email(message="Enter a valid email"),
        block_test_domain
    ])
    message = TextAreaField("Message", validators=[
        DataRequired(), Length(min=5)
    ])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    country = SelectField("Country", choices=[
        ('IN', 'India'), ('US', 'USA'), ('UK', 'UK')
    ], validators=[DataRequired()])
    terms = BooleanField("Accept Terms", validators=[DataRequired(message="You must accept terms")])
    password = PasswordField("Password", validators=[
        DataRequired(), Length(min=6)
    ])
    confirm = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    date = DateField("Date of Birth", validators=[Optional()])
    age = IntegerField("Age", validators=[
        DataRequired(), NumberRange(min=18, max=60, message="Age must be 18-60")
    ])
    username = StringField("Username", validators=[
        Length(min=6, message="Username must be more than 5 characters"),
        Optional()
    ])
    optional_note = StringField("Note", validators=[Optional()])
    submit = SubmitField("Submit")

if __name__ == '__main__':
    app.run(debug=True)
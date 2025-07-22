# 7. Event RSVP Form 
'''
Requirements: 
 Fields: Name, Email, Will Attend (BooleanField) 
 If not attending, show flash “Sorry to miss you”
 Use validators and show form validation errors clearly
'''

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import BooleanField

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  


class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
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
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email')  
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Feedback')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')


class BugReportForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    description = TextAreaField('Bug Description', validators=[DataRequired()])
    severity = RadioField('Severity', choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit Bug Report')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=20)])
    submit = SubmitField('Send Message')

class RSVPForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    will_attend = BooleanField('I will attend')
    submit = SubmitField('Submit RSVP')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.full_name.data}! You have registered successfully.", "success")
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
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        password = form.password.data.strip()

        
        if email == "admin@example.com" and password == "password123":
            flash("Login successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid credentials", "error")
    return render_template('login.html', form=form)


@app.route('/bug-report', methods=['GET', 'POST'])
def bug_report():
    form = BugReportForm()
    if form.validate_on_submit():
        severity = form.severity.data
        if severity == 'high':
            flash("⚠️ High severity bug submitted. We’ll prioritize this!", "high")
        elif severity == 'medium':
            flash("Medium severity bug submitted. We’ll check it soon.", "medium")
        else:
            flash("Low severity bug noted. Thank you!", "low")
        return redirect(url_for('bug_report'))
    return render_template('bug_report.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("📬 Your message has been sent. We'll get back to you soon!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        if not form.will_attend.data:
            flash("😢 Sorry to miss you.", "error")
        else:
            flash("🎉 Thanks for your RSVP. See you at the event!", "success")
        return redirect(url_for('rsvp'))
    return render_template('rsvp.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)

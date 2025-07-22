# 9. Course Enrollment Form 
'''
Requirements: 
 Fields: Student Name, Email, Course (SelectField), Age (IntegerField) 
 Age must be between 18 and 60 
 Flash dynamic message: “Hi [name], you enrolled in [course]” 
 Show all validation errors clearly
'''

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class EnrollmentForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    course = SelectField('Course', choices=[
        ('python', 'Python Programming'),
        ('web', 'Web Development'),
        ('data', 'Data Science')
    ], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=60)])
    submit = SubmitField('Enroll')

@app.route('/', methods=['GET', 'POST'])
def enroll():
    form = EnrollmentForm()
    if form.validate_on_submit():
        name = form.student_name.data
        course = form.course.data
        course_name = dict(form.course.choices).get(course)
        flash(f"Hi {name}, you enrolled in {course_name}!", "success")
        return redirect(url_for('enroll'))
    return render_template('enroll.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

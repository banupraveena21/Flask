# 15. Student Feedback Form (Course) 
'''
 Requirements: 
 Fields: Name, Email, Course, Rating (1-10), Suggestion 
 Validators for all except suggestion 
 Flash score-based message (e.g., if < 5: "We'll improve!") 
 Display all errors inline
'''

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def feedback_form():
    errors = {}
    values = {}

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        course = request.form.get('course', '').strip()
        rating = request.form.get('rating', '').strip()
        suggestion = request.form.get('suggestion', '').strip()

        values = {
            'name': name,
            'email': email,
            'course': course,
            'rating': rating,
            'suggestion': suggestion
        }

        # Validation
        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not course:
            errors['course'] = 'Course is required.'

        try:
            rating_val = int(rating)
            if rating_val < 1 or rating_val > 10:
                errors['rating'] = 'Rating must be between 1 and 10.'
        except ValueError:
            errors['rating'] = 'Rating must be an integer between 1 and 10.'

        if not errors:
            msg = "We'll improve!" if rating_val < 5 else "Thanks for your positive feedback!"
            flash(msg, 'success')
            return redirect(url_for('feedback_form'))

    return render_template('feedback_form.html', errors=errors, values=values)

if __name__ == '__main__':
    app.run(debug=True)
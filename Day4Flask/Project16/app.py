# 16. Survey Form 
'''
Requirements: 
 Fields: Age, Gender, Favorite Product (SelectField), Feedback 
 Age must be in 18–100 
 Use Flash for “Thanks for participating!” 
 Show styled error box at the top if form is invalid 
'''

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'supersecret'

GENDERS = ['Male', 'Female', 'Other']
PRODUCTS = ['Laptop', 'Phone', 'Tablet', 'Smartwatch']

@app.route('/', methods=['GET', 'POST'])
def survey():
    errors = {}
    values = {}

    if request.method == 'POST':
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '')
        product = request.form.get('product', '')
        feedback = request.form.get('feedback', '').strip()

        values = {'age': age, 'gender': gender, 'product': product, 'feedback': feedback}

        # Validation
        try:
            age_int = int(age)
            if age_int < 18 or age_int > 100:
                errors['age'] = 'Age must be between 18 and 100.'
        except ValueError:
            errors['age'] = 'Age must be a number.'

        if gender not in GENDERS:
            errors['gender'] = 'Please select a valid gender.'

        if product not in PRODUCTS:
            errors['product'] = 'Please select a product.'

        if not feedback or len(feedback) < 5:
            errors['feedback'] = 'Feedback is required.'

        if not errors:
            flash('Thanks for participating!', 'success')
            return redirect(url_for('survey'))

    return render_template('survey.html', errors=errors, values=values, genders=GENDERS, products=PRODUCTS)

if __name__=='__main__':
    app.run(debug=True)
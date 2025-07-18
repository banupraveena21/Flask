# 3. Student Result Dashboard 
'''
Requirements: 
 /result route displays a student’s name, marks, and grade 
 Use {% if %} to color-code grades (A, B, C) 
 Loop over subjects to show marks using {% for subject in subjects %} 
 Base layout with Bootstrap styling in base.html 
 CSS in static/style.css
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    student = {
        'name': 'Alice Johnson',
        'subjects': {
            'Math': 92,
            'Science': 85,
            'History': 76,
            'English': 88
        }
    }

    average = sum(student['subjects'].values()) / len(student['subjects'])

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    else:
        grade = 'C'

    return render_template('result.html', student=student, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
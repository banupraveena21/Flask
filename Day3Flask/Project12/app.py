from flask import Flask, render_template

app = Flask(__name__)

@app.route('/courses')
def courses():
    course_list = [
        {
            'title': 'Intro to Python',
            'instructor': 'Jane Doe',
            'duration': '4 weeks',
            'level': 'beginner'
        },
        {
            'title': 'Data Structures & Algorithms',
            'instructor': 'John Smith',
            'duration': '6 weeks',
            'level': 'intermediate'
        },
        {
            'title': 'Machine Learning Mastery',
            'instructor': 'Dr. Ada Lovelace',
            'duration': '8 weeks',
            'level': 'advanced'
        }
    ]
    return render_template('courses.html', courses=course_list)

if __name__ == '__main__':
    app.run(debug=True)

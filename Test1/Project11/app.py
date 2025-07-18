'''
11. Quiz Question Preview
•	Route /quiz/<question_id>
•	Display question text, options using Jinja2 loop
•	Template inheritance from base.html
•	Use CSS for styling choice
'''

from flask import Flask, render_template

app = Flask(__name__)


QUIZ_QUESTIONS = {
    '1': {
        'text': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid']
    },
    '2': {
        'text': 'Which language is primarily used for data science?',
        'options': ['Java', 'Python', 'C++', 'Swift']
    },
    '3': {
        'text': 'What planet is known as the Red Planet?',
        'options': ['Earth', 'Venus', 'Mars', 'Jupiter']
    }
}

@app.route('/')
def home():
    return render_template('home.html', questions=QUIZ_QUESTIONS)

@app.route('/quiz/<question_id>')
def quiz(question_id):
    question = QUIZ_QUESTIONS.get(question_id)
    if not question:
        return f"<h2>Question ID {question_id} not found.</h2>"
    return render_template('quiz.html', question=question, question_id=question_id)

if __name__ == '__main__':
    app.run(debug=True)

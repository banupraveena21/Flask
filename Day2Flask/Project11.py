# 11. Student Quiz Portal
'''
Requirements:
- /quiz: Form with name and 3 MCQ questions
- POST to /quiz-result and display answers
- Redirect using url_for() to /quiz-summary/<name>
- Filter score with /leaderboard?score=10
'''

from flask import Flask, request, redirect, url_for

app = Flask(__name__)


submissions = []


correct_answers = {
    'q1': 'b',
    'q2': 'a',
    'q3': 'c'
}


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        name = request.form.get('name')
        answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3')
        }
        score = sum(1 for q in correct_answers if answers[q] == correct_answers[q])

       
        submissions.append({'name': name, 'answers': answers, 'score': score})

        return redirect(url_for('quiz_summary', name=name))

    return '''
    <h2>Student Quiz</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>

        <strong>1. What is the capital of France?</strong><br>
        a) Berlin <input type="radio" name="q1" value="a" required><br>
        b) Paris <input type="radio" name="q1" value="b"><br>
        c) Rome <input type="radio" name="q1" value="c"><br><br>

        <strong>2. 2 + 2 = ?</strong><br>
        a) 4 <input type="radio" name="q2" value="a" required><br>
        b) 3 <input type="radio" name="q2" value="b"><br>
        c) 5 <input type="radio" name="q2" value="c"><br><br>

        <strong>3. Which is a programming language?</strong><br>
        a) Banana <input type="radio" name="q3" value="a" required><br>
        b) Elephant <input type="radio" name="q3" value="b"><br>
        c) Python <input type="radio" name="q3" value="c"><br><br>

        <input type="submit" value="Submit Quiz">
    </form>
    '''


@app.route('/quiz-summary/<name>')
def quiz_summary(name):
    user = next((u for u in submissions if u['name'].lower() == name.lower()), None)
    if not user:
        return f"<h3>No quiz data found for {name}</h3>", 404

    html = f"<h3>Quiz Summary for {user['name']}</h3>"
    html += f"<p><strong>Score:</strong> {user['score']} / 3</p><ul>"
    for q, a in user['answers'].items():
        html += f"<li>{q.upper()}: You answered '{a}' - {'Correct' if a == correct_answers[q] else 'Wrong'}</li>"
    html += "</ul>"
    return html


@app.route('/leaderboard')
def leaderboard():
    score_filter = request.args.get('score')
    if not score_filter:
        return "<p>Please provide a score to filter. Example: /leaderboard?score=3</p>"

    try:
        score_val = int(score_filter)
    except ValueError:
        return "<p>Invalid score value.</p>"

    matched = [s for s in submissions if s['score'] == score_val]
    if not matched:
        return f"<p>No students found with score = {score_val}</p>"

    html = f"<h3>Students with Score {score_val}</h3><ul>"
    for s in matched:
        html += f"<li>{s['name']}</li>"
    html += "</ul>"
    return html


if __name__ == '__main__':
    app.run(debug=True)
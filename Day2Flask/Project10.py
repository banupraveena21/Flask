# 10. Daily Mood Logger
'''
Requirements:
- /log-mood: Form with name, mood, and reason
- POST to /mood-result, show mood data
- Query route: /logs?mood=happy filters mood entries
- Redirect to /thank-you/<name> with dynamic message
'''

from flask import Flask, request, redirect, url_for

app = Flask(__name__)


mood_logs = []


@app.route('/log-mood', methods=['GET', 'POST'])
def log_mood():
    if request.method == 'POST':
        name = request.form.get('name')
        mood = request.form.get('mood')
        reason = request.form.get('reason')

        mood_logs.append({'name': name, 'mood': mood, 'reason': reason})
        print(f"[Mood Logged] {name}: {mood} - {reason}")

        return redirect(url_for('thank_you', name=name))
    
    return '''
    <h2>Daily Mood Logger</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Mood:
        <select name="mood" required>
            <option value="happy">Happy</option>
            <option value="sad">Sad</option>
            <option value="angry">Angry</option>
            <option value="neutral">Neutral</option>
        </select><br><br>
        Reason:<br>
        <textarea name="reason" rows="4" cols="30" required></textarea><br><br>
        <input type="submit" value="Log Mood">
    </form>
    '''


@app.route('/mood-result', methods=['POST'])
def mood_result():
    name = request.form.get('name')
    mood = request.form.get('mood')
    reason = request.form.get('reason')
    return f"<h3>{name} feels {mood} because: {reason}</h3>"


@app.route('/logs')
def view_logs():
    mood_filter = request.args.get('mood')
    filtered_logs = mood_logs if not mood_filter else [log for log in mood_logs if log['mood'].lower() == mood_filter.lower()]

    if not filtered_logs:
        return "<p>No mood entries found.</p>"

    html = "<h3>Mood Logs:</h3><ul>"
    for entry in filtered_logs:
        html += f"<li>{entry['name']} felt <strong>{entry['mood']}</strong>: {entry['reason']}</li>"
    html += "</ul>"
    return html


@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h3>Thank you, {name.title()}! Your mood has been logged.</h3>"


if __name__ == '__main__':
    app.run(debug=True)
# 8. Bug Reporting System
'''
Requirements:
- /report: Form with title, description, and priority (POST)
- /submit-report: Saves and redirects to /report-confirm
- /bugs?priority=high to filter reports
- /bug/<id> returns dynamic bug details
'''


from flask import Flask, request, redirect, url_for

app = Flask(__name__)


bugs = []
bug_id_counter = 1


@app.route('/report', methods=['GET'])
def report_form():
    return '''
    <h2>Report a Bug</h2>
    <form method="POST" action="/submit-report">
        Title: <input type="text" name="title" required><br><br>
        Description:<br>
        <textarea name="description" rows="5" cols="40" required></textarea><br><br>
        Priority:
        <select name="priority" required>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
        </select><br><br>
        <input type="submit" value="Submit Bug">
    </form>
    '''


@app.route('/submit-report', methods=['POST'])
def submit_report():
    global bug_id_counter

    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority')

    bug = {
        'id': bug_id_counter,
        'title': title,
        'description': description,
        'priority': priority
    }
    bugs.append(bug)
    bug_id_counter += 1

    print(f"[Bug Submitted] ID: {bug['id']} Title: {title} Priority: {priority}")

    return redirect(url_for('report_confirm'))


@app.route('/report-confirm')
def report_confirm():
    return "<h3>Thank you! Your bug report has been submitted.</h3>"


@app.route('/bugs')
def list_bugs():
    priority_filter = request.args.get('priority')
    filtered = bugs
    if priority_filter:
        filtered = [b for b in bugs if b['priority'].lower() == priority_filter.lower()]

    if not filtered:
        return "<p>No bugs found for the given criteria.</p>"

    html = "<h3>Bug Reports:</h3><ul>"
    for bug in filtered:
        html += f'<li><a href="/bug/{bug["id"]}">[{bug["priority"].title()}] {bug["title"]}</a></li>'
    html += "</ul>"
    return html


@app.route('/bug/<int:bug_id>')
def bug_details(bug_id):
    bug = next((b for b in bugs if b['id'] == bug_id), None)
    if not bug:
        return "<h3>Bug not found</h3>", 404

    return f'''
    <h3>Bug #{bug["id"]}: {bug["title"]}</h3>
    <p><strong>Priority:</strong> {bug["priority"].title()}</p>
    <p><strong>Description:</strong><br>{bug["description"]}</p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
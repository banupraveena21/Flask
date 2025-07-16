# 14. Online Donation Form
'''
Requirements:
- /donate: Form for name, amount, and purpose
- Submit to /donate-confirm (POST)
- Redirect to /thank-donor/<name>
- Query support like /donations?purpose=education
'''


from flask import Flask, request, redirect, url_for

app = Flask(__name__)


donations = []


@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form.get('name')
        amount = request.form.get('amount')
        purpose = request.form.get('purpose')

        
        donations.append({'name': name, 'amount': amount, 'purpose': purpose})

        
        return redirect(url_for('thank_donor', name=name))
    
    return '''
    <h2>Online Donation Form</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Amount (USD): <input type="number" name="amount" step="0.01" required><br><br>
        Purpose:
        <select name="purpose" required>
            <option value="education">Education</option>
            <option value="healthcare">Healthcare</option>
            <option value="environment">Environment</option>
        </select><br><br>
        <input type="submit" value="Donate">
    </form>
    '''




@app.route('/thank-donor/<name>')
def thank_donor(name):
    return f"<h3>Thank you, {name.title()}! Your donation makes a difference. 🙏</h3>"


@app.route('/donations')
def view_donations():
    purpose_filter = request.args.get('purpose')
    filtered = donations if not purpose_filter else [d for d in donations if d['purpose'] == purpose_filter.lower()]

    if not filtered:
        return "<p>No donations found for that purpose.</p>"

    html = f"<h3>Donations{' for ' + purpose_filter.title() if purpose_filter else ''}</h3><ul>"
    for d in filtered:
        html += f"<li>{d['name']} donated ${d['amount']} for {d['purpose'].title()}</li>"
    html += "</ul>"
    return html


if __name__ == '__main__':
    app.run(debug=True)
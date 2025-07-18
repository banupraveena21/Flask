from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('poll.html')

@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form.get('choice')
    if not choice:
        error = "Please select an option."
        return render_template('poll.html', error=error)
    return redirect(url_for('result', choice=choice))

@app.route('/result')
def result():
    choice = request.args.get('choice')
    if not choice:
        return redirect(url_for('home'))
    return render_template('result.html', choice=choice)

if __name__ == '__main__':
    app.run(debug=True)

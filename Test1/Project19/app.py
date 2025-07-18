from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/preview', methods=['POST'])
def preview():
    title = request.form.get('title', '')
    body = request.form.get('body', '')
    # Jinja2 will escape by default to prevent unsafe HTML rendering
    return render_template('preview.html', title=title, body=body)

if __name__ == '__main__':
    app.run(debug=True)

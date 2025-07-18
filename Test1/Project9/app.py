from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', 'Unknown')
        age = request.form.get('age', 'N/A')
        hobbies_raw = request.form.get('hobbies', '')
        hobbies = [h.strip() for h in hobbies_raw.split(',') if h.strip()]
        return render_template('bio.html', name=name, age=age, hobbies=hobbies)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

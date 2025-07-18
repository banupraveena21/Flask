'''
6. Student Introduction Page
•	Route: /student/<name>?age=20&course=Python
•	Show student bio using dynamic routing and query params
•	Use Jinja2 to dynamically fill card content
•	Base template reused
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<name>')
def student(name):
    age = request.args.get('age', 'Unknown')
    course = request.args.get('course', 'Not specified')
    
    return render_template('student.html', name=name, age=age, course=course)

if __name__ == '__main__':
    app.run(debug=True)

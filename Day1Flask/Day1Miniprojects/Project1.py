# 1. Digital Visiting Card
'''
Requirements:
• Home page: / returns your name, profession, and contact info in HTML.
• About route: /about explains your background.
• /skills/<name> returns a list of skills for that person.
• Install Flask and run using both python app.py and flask run.
'''

from flask import Flask, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return """
    <h1>Banu Praveena</h1>
    <p>Profession: Software Developer</p>
    <p>Contact: banupraveena21@gmail.com</p>
    """

# About page
@app.route('/about')
def about():
    return """
    <h2>About Me</h2>
    <p>I am a passionate software developer in building web applications.</p>
    """

# Skills route
@app.route('/skills/<name>')
def skills(name):
    skills_data = {
        'banu': ['Python', 'Flask', 'JavaScript', 'SQL'],
        'praveena': ['Java', 'Spring Boot', 'React', 'AWS'],
        'guna': ['C++', 'Machine Learning', 'TensorFlow'],
    }
    person_skills = skills_data.get(name.lower())
    if person_skills:
        return jsonify({name: person_skills})
    else:
        return jsonify({"error": "Person not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

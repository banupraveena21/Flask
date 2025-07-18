# 1. Personal Portfolio Website 
'''
 Requirements: 
 Pages: Home, About, Projects, Contact — each extending base.html 
 Render name, skills, and project list via render_template() 
 Loop over project data using {% for %} 
 Show "Available for hire" message using {% if %} 
 Link external CSS and include an image in static/
'''

from flask import Flask, render_template

app = Flask(__name__)


name = "Banu Praveena"
skills = ["Python", "Flask", "JavaScript", "HTML", "CSS"]
projects = [
    {"title": "Portfolio Website", "description": "A personal website built using Flask."},
    {"title": "Task Manager", "description": "An app to manage daily tasks."}
]
available_for_hire = True

@app.route('/')
def home():
    return render_template('home.html', name=name, available=available_for_hire)

@app.route('/about')
def about():
    return render_template('about.html', name=name, skills=skills)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

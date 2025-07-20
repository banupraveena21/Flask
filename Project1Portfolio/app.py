# Personal Portfolio Website
'''
1.	Homepage, About, Projects, Contact pages via routes.
2.	Contact form (POST, request.form), success redirect.
3.	Dynamic project page: /project/.
4.	Jinja2 for project listing (loop).
5.	Base template, custom CSS in static/.
6.	Query args for filtering projects by tag.
'''

from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load project data
with open('data/projects.json') as f:
    projects = json.load(f)

@app.route('/')
def home():
    featured = projects[:2]
    return render_template('home.html', projects=featured)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project_list():
    tag = request.args.get('tag')
    filtered = [p for p in projects if tag in p['tags']] if tag else projects
    return render_template('projects.html', projects=filtered)

@app.route('/project/<slug>')
def project_detail(slug):
    project = next((p for p in projects if p['slug'] == slug), None)
    if not project:
        return "Project not found", 404
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        # Normally you'd handle or store the form data here
        return redirect(url_for('contact_success'))
    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return "<h1>Thank you for contacting me!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
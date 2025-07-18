from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


profiles = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        skills = request.form['skills']
        bio = request.form['bio']
        
       
        profiles[name] = {
            'skills': skills,
            'bio': bio
        }
        return redirect(url_for('profile', name=name))
    
    return render_template('home.html')

@app.route('/profile/<name>')
def profile(name):
    if name not in profiles:
        return "Profile not found", 404
    return render_template('profile.html', name=name, profile=profiles[name])

if __name__ == '__main__':
    app.run(debug=True)

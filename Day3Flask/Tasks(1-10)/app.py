# Setting up HTML templates in the templates/ folder  
# 2. Render the index.html from a Flask route using render_template(). 
# 4. Modify index.html to show a simple heading and a paragraph. 
# 6. Move all .html files into the templates/ folder and confirm Flask loads them correctly. 
# 8. Add a navigation bar in index.html linking to /about, /contact, and /. 
# 9. Pass a variable from Flask to index.html (e.g., username) and display it. 
# 10. Include a page title in each template using <title>{{ title }}</title>.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    username = "Banu Praveena"
    return render_template('index.html', title="Home", username=username)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contacts.html', title="Contact")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

if __name__ == '__main__':
    app.run(debug=True)
# Static files: CSS, JS, Images in static/ folder  
# 1. Create a static/ folder and add a style.css file. 
# 2. Link style.css in your base.html using {{ url_for('static', filename='style.css') }}. 
# 3. Add a static image to static/images/ and display it in about.html. 
# 4. Add a JavaScript file (main.js) and link it in the template. 
# 5. Use inline CSS in HTML, then move it to style.css and clean up inline styles.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
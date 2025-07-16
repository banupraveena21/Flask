# Simple Text Banner Generator
'''
Requirements:
• / displays “Enter your banner text” with a link to /banner/Hello.
• /banner/<text> returns large <h1> HTML with the input string.
• Add another route /banner/<text>/<size> to change size (h1-h6).
• Create routes dynamically with <string> path variables.
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <p>Enter your banner text:</p>
    <a href="/banner/Hello">Try "Hello"</a>
    '''

@app.route("/banner/<string:text>")
def banner_default(text):
    return f"<h1>{text}</h1>"

@app.route("/banner/<string:text>/<string:size>")
def banner_custom(text, size):
    size = size.lower()
    if size in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        return f"<{size}>{text}</{size}>"
    else:
        return f"<p>Invalid size '{size}'. Use h1 to h6.</p>"

if __name__ == "__main__":
    app.run(debug=True)
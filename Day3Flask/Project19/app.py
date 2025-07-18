from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page! <a href='/cause-error'>Cause Error</a>"

@app.route('/cause-error')
def cause_error():
    # This route will intentionally raise an error for testing 500
    raise Exception("Intentional server error!")

# Custom 404 handler
@app.errorhandler(404)
def page_not_found(e):
    message = "Oops! The page you are looking for does not exist."
    return render_template('404.html', error_code=404, message=message), 404

# Custom 500 handler
@app.errorhandler(500)
def internal_error(e):
    message = "Sorry, something went wrong on our end."
    return render_template('500.html', error_code=500, message=message), 500

if __name__ == '__main__':
    app.run(debug=True)

# Age Checker App
'''
Requirements:
• /age/<name>/<year> returns “Hi [name], you are [age] years old”.
• Validate the year to be < current year.
• Run on custom port and IP using flask run --port=5050 --host=0.0.0.0.
• Use triple quotes to return HTML.
'''


from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/age/<string:name>/<int:year>")
def age_checker(name, year):
    current_year = datetime.now().year

    if year >= current_year:
        return """
        <h2 style="color:red;">Invalid year!</h2>
        <p>Please enter a birth year less than the current year.</p>
        """

    age = current_year - year
    return f"""
    <html>
        <body style="font-family:sans-serif; background-color:#f9f9f9; padding:20px;">
            <h2 style="color:green;">Hi {name.title()}!</h2>
            <p>You are <b>{age}</b> years old.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
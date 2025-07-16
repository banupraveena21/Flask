# Zodiac Sign Generator
'''
Requirements:
• /zodiac/<date> returns Zodiac sign based on date (dummy logic).
• /zodiac/help explains format to enter date.
• Use string splitting logic to process /zodiac/2000-12-25.
• Add inline HTML + <strong>, <i>, <hr>.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/zodiac/help")
def zodiac_help():
    return """
    <h2>Zodiac Sign Help</h2>
    <p>Please enter your birth date in this format: <strong>YYYY-MM-DD</strong></p>
    <p>Example: <code>/zodiac/1999-03-25</code></p>
    <hr>
    """

@app.route("/zodiac/<string:date>")
def zodiac_sign(date):
    try:
        year, month, day = date.split("-")
        month = int(month)
        day = int(day)
    except ValueError:
        return "<p style='color:red;'><strong>Invalid date format!</strong> Use YYYY-MM-DD.</p>"

    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        sign = "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        sign = "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        sign = "Gemini"
    else:
        sign = "Zodiac sign not implemented for this date"

    return f"""
    <h2>Your Zodiac Sign</h2>
    <p><strong>Date of Birth:</strong> {date}</p>
    <p><i>Your sign is:</i> <strong>{sign}</strong></p>
    <hr>
    """

if __name__ == "__main__":
    app.run(debug=True)
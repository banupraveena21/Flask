# Daily Quote Viewer
'''
Requirements:
• / shows today's quote (hardcoded list of 7 quotes).
• /quote/<day> returns quote for that day (monday, tuesday, etc.)
• Add inline CSS for styling the quotes.
• Use virtual environment + pip installation.
'''

from flask import Flask
from datetime import datetime

app = Flask(__name__)

quotes = {
    "monday":    "Start your week strong!",
    "tuesday":   "Keep the momentum going!",
    "wednesday": "Halfway there. Stay focused!",
    "thursday":  "Push through, you're doing great!",
    "friday":    "Finish strong!",
    "saturday":  "Relax and recharge.",
    "sunday":    "Plan and prepare for the week ahead."
}

def get_today_day():
    return datetime.now().strftime("%A").lower()

@app.route("/")
def today_quote():
    day = get_today_day()
    quote = quotes.get(day, "No quote available.")
    return f"""
    <h2 style="color: teal; font-family: Arial;">Quote for Today ({day.title()}):</h2>
    <p style="font-size: 20px; color: gray;">"{quote}"</p>
    """

@app.route("/quote/<string:day>")
def quote_by_day(day):
    day = day.lower()
    quote = quotes.get(day)
    if quote:
        return f"""
        <h2 style="color: darkblue; font-family: Georgia;">Quote for {day.title()}:</h2>
        <p style="font-size: 20px; color: darkslategray;">"{quote}"</p>
        """
    else:
        return f"<p style='color:red;'>No quote found for '{day}'</p>"

if __name__ == "__main__":
    app.run(debug=True)
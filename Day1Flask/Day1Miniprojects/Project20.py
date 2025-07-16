# Health Reminder Display
'''
Requirements:
• /reminder/<hour> gives health advice based on hour (e.g., drink water, stretch).
• /reminder/help explains usage.
• Use simple logic to rotate messages based on hour input.
'''


from flask import Flask

app = Flask(__name__)

# Simple health advice rotating based on hour (0-23)
health_tips = [
    "Drink a glass of water 💧",
    "Take a short walk 🚶‍♂️",
    "Do some stretching exercises 🧘‍♀️",
    "Rest your eyes for a few minutes 👀",
    "Eat a healthy snack 🍎",
    "Practice deep breathing 🌬️"
]

@app.route("/reminder/<int:hour>")
def reminder(hour):
    if hour < 0 or hour > 23:
        return "<p style='color:red;'>Please enter a valid hour (0–23).</p>"

    tip = health_tips[hour % len(health_tips)]
    return f"""
    <h2 style="color:green;">Health Reminder for Hour {hour}</h2>
    <p style="font-size:18px;">{tip}</p>
    """

@app.route("/reminder/help")
def reminder_help():
    return """
    <h3>Health Reminder Help</h3>
    <p>Use the route <code>/reminder/&lt;hour&gt;</code> where hour is between 0 and 23.</p>
    <p>Example: <code>/reminder/14</code></p>
    <hr>
    """

if __name__ == "__main__":
    app.run(debug=True)
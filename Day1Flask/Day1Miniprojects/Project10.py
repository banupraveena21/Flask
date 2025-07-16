# Motivational Message Rotator
'''
Requirements:
• /message returns a different motivational quote every time (from list).
• Add /message/<index> to manually select message by index.
• Make the response colorful with basic CSS in HTML.
• Practice Flask dev server rerun behavior.
'''

from flask import Flask
import random

app = Flask(__name__)

# List of motivational messages
messages = [
    "Believe you can and you're halfway there.",
    "Every day is a second chance.",
    "Push yourself, because no one else is going to do it for you.",
    "You are stronger than you think.",
    "Dream it. Wish it. Do it.",
    "Stay positive, work hard, make it happen.",
    "The best time to start was yesterday. The next best time is now."
]

@app.route("/message")
def random_message():
    quote = random.choice(messages)
    return f"""
    <div style="background-color:#f0f8ff;padding:20px;border-radius:10px;font-family:sans-serif;">
        <h2 style="color:#2e8b57;">Motivational Message</h2>
        <p style="font-size:20px;color:#333;"><em>{quote}</em></p>
    </div>
    """

@app.route("/message/<int:index>")
def message_by_index(index):
    if 0 <= index < len(messages):
        quote = messages[index]
        return f"""
        <div style="background-color:#fff8dc;padding:20px;border-radius:10px;font-family:sans-serif;">
            <h2 style="color:#8b0000;">Motivational Message #{index}</h2>
            <p style="font-size:20px;color:#444;"><em>{quote}</em></p>
        </div>
        """
    else:
        return f"<p style='color:red;'>Invalid index. Please choose 0 to {len(messages) - 1}.</p>"

if __name__ == "__main__":
    app.run(debug=True)
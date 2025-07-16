# BMI Calculator (Text Output Only)
'''
Requirements:
• / shows usage info.
• /bmi/<weight>/<height> calculates and returns BMI value and category.
• Demonstrate multiple route returns.
• Explain why Flask is good for small tools like this.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>BMI Calculator</h2>
    <p>Usage: Go to <code>/bmi/&lt;weight&gt;/&lt;height&gt;</code></p>
    <p><b>Example:</b> /bmi/70.0/1.75</p>
    """

@app.route("/bmi/<float:weight>/<float:height>")
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return (
        f"<h3>Your BMI is: {bmi:.2f}</h3>"
        f"<p>Category: <b>{category}</b></p>"
    )

if __name__ == "__main__":
    app.run(debug=True)

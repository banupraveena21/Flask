# Simple Calculator (in URL)
'''
Requirements:
• /calc/<op>/<num1>/<num2> performs operation: add, sub, mul, div.
• Add validation for division by zero.
• Add an /ops route that lists valid operations.
• Return results with <h2> headers.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/calc/<op>/<float:num1>/<float:num2>")
def calculate(op, num1, num2):
    result = None

    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        if num2 == 0:
            return "<h2 style='color:red;'>Error: Division by zero is not allowed.</h2>"
        result = num1 / num2
    else:
        return f"<h2 style='color:red;'>Invalid operation: {op}</h2>"

    return f"""
    <h2>Operation: {op}</h2>
    <h2>Operands: {num1} and {num2}</h2>
    <h2>Result: {result}</h2>
    """

@app.route("/ops")
def list_ops():
    return """
    <h2>Supported Operations</h2>
    <ul>
        <li><strong>add</strong> - Addition</li>
        <li><strong>sub</strong> - Subtraction</li>
        <li><strong>mul</strong> - Multiplication</li>
        <li><strong>div</strong> - Division</li>
    </ul>
    <p>Example: <code>/calc/add/10.0/5.0</code></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
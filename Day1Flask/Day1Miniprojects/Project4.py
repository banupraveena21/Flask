# Personalized Greeting App
'''
Requirements:
• /hello/<name> displays “Hello, [name]!”.
• /greet/<name>/<time> returns “Good Morning [name]” or “Good Evening” based on the time argument.
• Use routes with multiple dynamic segments.
• Add debug=True and change content live.
'''


from flask import Flask

app = Flask(__name__)

@app.route("/hello/<string:name>")
def hello(name):
    return f"<h2>Hello, {name}!</h2>"

@app.route("/greet/<string:name>/<string:time>")
def greet(name, time):
    time = time.lower()
    if time in ["morning", "am"]:
        greeting = "Good Morning"
    elif time in ["evening", "pm", "night"]:
        greeting = "Good Evening"
    else:
        greeting = "Hello"

    return f"<h3>{greeting}, {name}!</h3>"

if __name__ == "__main__":
    app.run(debug=True)

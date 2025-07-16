# Word Counter App
'''
Requirements:
• /wordcount/<text> counts and returns number of words in the input text.
• /wordcount/help explains how to use the route.
• Add header and paragraph styling with basic CSS in return string.
'''


from flask import Flask

app = Flask(__name__)

@app.route("/wordcount/<path:text>")
def count_words(text):
    word_list = text.split()
    word_count = len(word_list)

    return f"""
    <div style="font-family:Arial; background-color:#f0f8ff; padding:20px; border-radius:8px;">
        <h2 style="color:#2e8b57;">Word Counter</h2>
        <p style="font-size:18px;"><strong>Input Text:</strong> {text}</p>
        <p style="font-size:18px;"><strong>Word Count:</strong> {word_count}</p>
    </div>
    """

@app.route("/wordcount/help")
def help_page():
    return """
    <div style="font-family:Arial; background-color:#fff0f5; padding:20px; border-radius:8px;">
        <h2 style="color:#8b0000;">Word Counter Help</h2>
        <p style="font-size:16px;">Use the route <code>/wordcount/&lt;text&gt;</code> to count words in a sentence.</p>
        <p style="font-size:16px;"><strong>Example:</strong> <code>/wordcount/This is a test</code></p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
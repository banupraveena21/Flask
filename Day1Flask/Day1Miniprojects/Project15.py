# Text Mirror Tool
'''
Requirements:
• /mirror/<text> returns original and reversed text.
• Use <pre> tag to show formatted output.
• Add a table showing: Original, Reversed, Length.
• Use Flask routes only, no templates yet.
'''


from flask import Flask

app = Flask(__name__)

@app.route("/mirror/<path:text>")
def mirror_text(text):
    reversed_text = text[::-1]
    length = len(text)

    return f"""
    <h2 style="font-family:Arial; color:#4682b4;">Text Mirror Tool</h2>
    <pre>
+------------+----------------------+--------+
|  Original  |       Reversed       | Length |
+------------+----------------------+--------+
| {text} | {reversed_text} |   {length}   |
+------------+----------------------+--------+
    </pre>
    <hr>
    <p style="font-family:Arial; font-size:14px; color:#555;">Use <code>/mirror/&lt;text&gt;</code> to mirror any input.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
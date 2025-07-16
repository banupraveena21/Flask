# URL Short Previewer
'''
Requirements:
• /preview/<site> returns dummy preview text like “This is [site].com website.”
• Return HTML with <h1>, <p>, and simulated preview.
• Use routes to simulate preview of Google, YouTube, etc.
'''


from flask import Flask

app = Flask(__name__)

# Dummy previews for some sites
previews = {
    "google": "Google is a search engine giant offering countless services worldwide.",
    "youtube": "YouTube is the largest video-sharing platform on the planet.",
    "facebook": "Facebook connects billions of people through social networking."
}

@app.route("/preview/<site>")
def preview(site):
    site_lower = site.lower()
    preview_text = previews.get(site_lower, f"This is {site_lower}.com website.")

    return f"""
    <h1>Preview of {site_lower.capitalize()}</h1>
    <p>{preview_text}</p>
    <div style="border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9; width: 50%; font-family: Arial;">
        <strong>Simulated Preview:</strong>
        <p><i>Welcome to the {site_lower}.com homepage! Explore content, features, and more.</i></p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
# Static Portfolio Page Generator
'''
Requirements:
• /portfolio/<name> returns an HTML profile.
• Include 2 more routes: /portfolio/<name>/skills and /portfolio/<name>/projects.
• Use lists/HTML tables in the response.
• Start from scratch after uninstalling and reinstalling Flask.
'''

from flask import Flask

app = Flask(__name__)

user_data = {
    "banu": {
        "skills": ["Python", "Flask", "HTML", "CSS"],
        "projects": [
            {"name": "Portfolio Website", "tech": "Flask"},
            {"name": "Blog CMS", "tech": "Django"}
        ]
    },
    "guna": {
        "skills": ["JavaScript", "React", "Node.js"],
        "projects": [
            {"name": "E-commerce App", "tech": "React"},
            {"name": "Chat App", "tech": "Node.js"}
        ]
    }
}

@app.route("/portfolio/<string:name>")
def portfolio(name):
    name = name.lower()
    if name in user_data:
        return f"""
        <h1>{name.title()}'s Portfolio</h1>
        <p>Welcome to the personal portfolio page of <b>{name.title()}</b>.</p>
        <p><a href="/portfolio/{name}/skills">View Skills</a></p>
        <p><a href="/portfolio/{name}/projects">View Projects</a></p>
        """
    else:
        return f"<h2>User '{name}' not found.</h2>"

@app.route("/portfolio/<string:name>/skills")
def skills(name):
    name = name.lower()
    skills = user_data.get(name, {}).get("skills", [])
    if skills:
        skills_list = "".join(f"<li>{skill}</li>" for skill in skills)
        return f"""
        <h2>{name.title()}'s Skills</h2>
        <ul>{skills_list}</ul>
        """
    else:
        return f"<p>No skills found for '{name}'.</p>"

@app.route("/portfolio/<string:name>/projects")
def projects(name):
    name = name.lower()
    projects = user_data.get(name, {}).get("projects", [])
    if projects:
        table_rows = "".join(
            f"<tr><td>{p['name']}</td><td>{p['tech']}</td></tr>" for p in projects
        )
        return f"""
        <h2>{name.title()}'s Projects</h2>
        <table border="1" cellpadding="5">
            <tr><th>Project</th><th>Technology</th></tr>
            {table_rows}
        </table>
        """
    else:
        return f"<p>No projects found for '{name}'.</p>"

if __name__ == "__main__":
    app.run(debug=True)

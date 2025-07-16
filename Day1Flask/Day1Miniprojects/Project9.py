# Server Info Dashboard
'''
Requirements:
• / returns system information like IP, port, environment.
• /status returns "Running in Debug Mode" if enabled.
• Change port from 5000 to 8000 manually.
• Use .env file to define FLASK_APP and FLASK_DEBUG.
'''

from flask import Flask, request
import os
import socket

app = Flask(__name__)

@app.route("/")
def info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    port = request.environ.get('SERVER_PORT', 'unknown')
    debug_mode = app.debug
    environment = os.environ.get('FLASK_ENV', 'production')

    return f"""
    <h2>Server Info Dashboard</h2>
    <ul>
        <li><b>IP Address:</b> {ip}</li>
        <li><b>Port:</b> {port}</li>
        <li><b>Debug Mode:</b> {debug_mode}</li>
        <li><b>Environment:</b> {environment}</li>
    </ul>
    """

@app.route("/status")
def status():
    if app.debug:
        return "<p>Running in Debug Mode</p>"
    else:
        return "<p>Running in Production Mode</p>"

if __name__ == "__main__":
    # Manually override port to 8000
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=8000)
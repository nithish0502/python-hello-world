from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
    <body>
        <h1>Hello from Python-Hello-World! You’re deploying your first app</h1>
        <p>This is the latest version 2.0 deployed via Gunicorn + Docker + HTTPS.</p>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

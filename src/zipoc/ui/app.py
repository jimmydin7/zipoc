from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Zipoc Repository Viewer</h1>
    <p>Welcome! Commit history and changes will be displayed here.</p>
    """

def run_server():
    print("Starting Zipoc viewer at http://localhost:8080")
    app.run(port=8080, debug=False)

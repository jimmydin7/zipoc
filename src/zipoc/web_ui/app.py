from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

def run_server():

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    print("Starting Zipoc viewer...")
    app.run(port=8080, debug=False, use_reloader=False)
    print("Zipoc viewer running at http://localhost:8080")

if __name__ == "__main__":
    run_server()

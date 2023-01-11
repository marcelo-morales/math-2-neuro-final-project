import setup_analysis

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    health_list = setup_analysis.hospitalWorkerList
    return "<p>Hello, World!</p>"


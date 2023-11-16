from flask import Flask
from model import get_random_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return get_random_response("Greeting")

app.run()
from flask import Flask, request
from service import give_answer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/answer", methods=['POST'])
def get_answer():
    data = request.json

    answer = give_answer(data["message"])

    return answer

app.run()
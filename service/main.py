from flask import Flask, request
from flask_cors import CORS
from bot import process_message

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/message', methods=['POST'])
def getResponse():

    data = request.json
    message = data['message']

    result = process_message(message)

    return result

if __name__ == '__main__':
    app.run()
from flask import Flask, request
import os
from jarvis import Jarvis
from message import Telegram
from flask_cors import CORS


app = Flask(__name__)
jarvis = Jarvis()
telegram = Telegram()

CORS(app, origins=['https://josephdavidson.dev'])

@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    response = jarvis.ask(request_data['question'])
    return response


@app.route('/telegram', methods=['POST'])
def sendTelegram():
    request_data = request.get_json()
    message = request_data['message']
    responce = telegram.send(message)
    return responce


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
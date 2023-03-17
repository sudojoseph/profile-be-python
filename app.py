from flask import Flask, request
import os
from jarvis import Jarvis
from flask_cors import CORS


app = Flask(__name__)
jarvis = Jarvis()

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    response = jarvis.ask(request_data['question'])
    return response

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
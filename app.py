from flask import Flask, request
from jarvis import Jarvis


app = Flask(__name__)
jarvis = Jarvis()

@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    response = jarvis.ask(request_data['question'])
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
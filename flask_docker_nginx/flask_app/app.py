from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)

@server.route('/hello', methods=['GET'])
def hello():
    if request.method == 'GET':
        return 'Hello World!!!'
    else:
        return run_request()


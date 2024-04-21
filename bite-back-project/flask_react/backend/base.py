from flask import Flask, request, jsonify
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route('/profile/', methods=['POST'])
def my_profile():
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
        "result": request.json['food1Name']
    }

    return response_body
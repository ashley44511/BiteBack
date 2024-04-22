from flask import Flask, request, jsonify
from flask_cors import CORS
from main import Main
from graphPickle import Graph
from hashPickle import HashTable 

api = Flask(__name__)
CORS(api)

@api.route('/profile/', methods=['POST'])
def my_profile():
    main = Main()
    graphTime = main.mainImportVersion()
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
        "result": request.json['food1Name'],
        "graphTime": graphTime
    }

    return response_body

if __name__ == "__main__":
    main = Main()
    main.mainImportVersion()
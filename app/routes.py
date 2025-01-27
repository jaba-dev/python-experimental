from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

@main.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"received": data})

from flask import Flask, jsonify, request
from functions import *

app = Flask(__name__)

@app.route('/name/<string:name>', methods=['GET'])
def search_name_API(name):
    if request.method == 'GET':
        return search_name(name), 200
    return jsonify({"msg": "Not defined"}), 400


@app.route('/', methods=['POST'])
def search_name_JSON():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        name = request.get_json()['name']
        return search_name(name), 200
        
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug=True) 

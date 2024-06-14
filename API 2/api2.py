import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api2', methods=['GET'])
def call_api1():
    response = requests.get('http://api1:5001/api1')
    return jsonify({"message": response.text}), response.status_code

if __name__ == '__main__':
    app.run(port=5002)

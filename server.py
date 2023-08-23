from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello world!", 200

@app.route('/calculator/add', methods=['POST'])
def add():
    req = request.get_json()
    num1 = req['first']
    num2 = req['second']
    result = num1 + num2
    return jsonify({"result": result}), 200

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    req = request.get_json()
    num1 = req['first']
    num2 = req['second']
    result = num1 - num2
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

from flask import Flask, request, jsonify
from simple_chatbot import chatbot
app = Flask(__name__)

@app.route('/')
def hello_world():
    message = 'Hello, world! This is simple-chatbot!'
    return message

@app.route('/post', methods=['POST'])
def hello_post():
    message = 'Hello, POST! This is simple-chatbot!'
    return message

@app.route('/put', methods=['PUT'])
def hello_put():
    message = 'Hello, PUT! This is simple-chatbot!'
    return message

@app.route('/delete', methods=['DELETE'])
def hello_delete():
    message = 'Hello, DELETE! This is simple-chatbot!'
    return message

@app.route('/chatbot')
def reply():
    sentence = request.args.get('sentence')

    return jsonify(chatbot(sentence))
 
if __name__ == "__main__":
    app.run(debug=True, port='5000')

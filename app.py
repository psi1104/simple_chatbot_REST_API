from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    message = '''
              Hello, world! 
              This is simple-chatbot! 
              Please 
              '''
    return message

@app.route('/chatbot')
def chatbot():
    sentence = request.args.get('sentence')
    reply = ""

    if sentence == "Hello":
        reply = "Hi!"

    return jsonify({
                    "sentence":sentence,
                    "reply":reply
                    })
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')

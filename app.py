from flask import Flask, request, jsonify
app = Flask(__name__)
 
@app.route('/chatbot')
def chatbot():
    sentence = request.args.get('sentence')
    return jsonify({"sentence":sentence})
 
 
if __name__ == "__main__":
    app.run(port='5000')

from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def generate_response_api():
    

    return jsonify({"message": "hello world"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

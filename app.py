from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
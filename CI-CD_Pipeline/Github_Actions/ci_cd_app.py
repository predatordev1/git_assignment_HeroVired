from flask import Flask, jsonify, request

ci_cd_app = Flask(__name__)

@ci_cd_app.route("/", methods=["GET"])
def health_check():
    return "Flask app is running!"

@ci_cd_app.route("/contact", methods=["POST", "GET"])
def Hello():
    return "Hello Devendra"

if __name__ == '__main__':
    ci_cd_app.run(host='0.0.0.0', port=5000, debug=False)

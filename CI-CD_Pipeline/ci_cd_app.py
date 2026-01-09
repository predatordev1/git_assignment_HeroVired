from flask import Flask, jsonify, request

ci_cd_app = Flask(__name__)

@ci_cd_app.route("/contact", methods = ["POST", "GET"])
def Hello():
    return("Hello Devendra")

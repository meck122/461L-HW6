"""app.py: A Flask app that interacts with a React app and can be deployed to Heroku"""
__author__ = "Mark Liao"
__date__ = "03/27/2022"

from flask import Flask, jsonify
from flask.helpers import send_from_directory

# comment out on deployment
from flask_cors import CORS

# uses 'frontend' because that is where our react app is stored
app = Flask(__name__, static_folder="frontend/build", static_url_path="")

# comment out on deployment
CORS(app)

@app.route("/textbox/<first_name>", methods=["GET"])
def process_name(first_name: str):
    db = {
        'mark': 'liao'
    }
    if first_name.lower() in db:
        print('thats the right name!')
        return jsonify(last_name=db[first_name.lower()])
    else:
        return jsonify(last_name='User Not Found')

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
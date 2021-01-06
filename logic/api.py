from flask import Flask
from flask_cors import CORS

# from model import classify
from flask import request


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route("/", methods=["GET", "POST"])
def index():
    # label = classify(url)
    data = request.get_json()
    print(data)
    # return {"label": str(label)}
    return {"ans": "hello"}

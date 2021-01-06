from flask import Flask

# from model import classify
from flask import request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # label = classify(url)
    data = request.get_json()
    print(data)
    # return {"label": str(label)}
    return {"ans": "hello"}

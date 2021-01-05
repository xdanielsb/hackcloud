from flask import Flask
from model import classify

app = Flask(__name__)


@app.route("/<url>")
def index(url):
    label = classify(url)
    return {"label": str(label)}


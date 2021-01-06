from io import BytesIO

import cv2
import numpy as np
from flask import Flask, request
from flask_cors import CORS
from model import classify

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route("/", methods=["GET", "POST"])
def index():
    photo = request.files["file"]
    in_memory_file = BytesIO()
    photo.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
    label = classify(cv2.imdecode(data, 1))
    return {"label": str(label)}

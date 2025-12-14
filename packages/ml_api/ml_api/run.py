from flask import Flask
from .predict import predict
from .config import __version__, DEBUG, HOST, PORT
from .logging_config import logger

app = Flask(__name__)

@app.route("/version", methods=["GET"])
def version():
    return {"version": __version__}

from flask import request

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    input_json = request.get_json()
    data = input_json["data"]   
    return predict(data)        

if __name__ == "__main__":
    app.run(debug=True)
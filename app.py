import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return jsonify({"about": "hello world"})

@app.route('/predict_api',methods=['GET', 'POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    if request.method == "GET":
        return jsonify({"error": "you did not provide data"})
    else:
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])
        output = prediction[0]
        return jsonify({"received": data, "prediction": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

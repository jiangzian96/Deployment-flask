import numpy as np
from flask import Flask, json, request, jsonify, render_template
import pickle
import argparse

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return "Hello"


@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


@app.route('/predict/<exp>:<test>:<interview>')
def predict(exp, test, interview):
    prediction = model.predict(np.array([int(exp), int(test), int(interview)]).reshape(1, -1))
    output = round(prediction[0], 2)

    return jsonify({"salary": output})


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
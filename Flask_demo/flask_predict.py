# creating a Flask API with the already saved model

import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger

with open('rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# giving the name for the API
app = Flask(__name__)
swagger = Swagger(app)


# generator
@app.route('/predict')
def predict_iris():  # function for prediction
    """ Example endpoint returning the prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))

    return str(prediction)


# generator
@app.route('/predict_file', methods=['POST'])
def predict_iris_file():  # function for prediction
    """ Example file endpoint returning the prediction of iris
        ---
        parameters:
          - name: input_file
            in: formData
            type: file
            required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))


# running the API
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

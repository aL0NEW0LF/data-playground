import json
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

@app.route("/process/file/tojson", methods=['GET', 'POST'])
def dataframe_to_json():
    try:
        file_path = request.files['datafile']
        
        print(file_path.filename)

        if file_path.filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.filename.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.filename.endswith('.json'):
            df = pd.read_json(file_path)
        elif file_path.filename.endswith('.txt'):
            df = pd.read_csv(file_path, sep='\t')
        else:
            return Response('File type not supported', status=400)

        responseJSON = df.to_json(orient='records')
        
        print(responseJSON)

        response = Response(response=responseJSON, status=200, mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
        response.headers['Access-Control-Allow-Credentials'] = True

        print(response)

        return response
    
    except Exception as e:
        return Response(response=str(e), status=500)

@app.route("/rand", methods=['GET'])
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
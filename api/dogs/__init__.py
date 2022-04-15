import logging

import azure.functions as func
import requests
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = os.environ['PREDICTION_URL']
    file = req.files["file"]
    content = file.stream.read()
    
    headers = {
        'Prediction-Key': os.environ['PREDICTION_KEY'],
        'Content-Type': 'application/octet-stream'
        }

    data = requests.post(url, headers=headers, data = content)
    return func.HttpResponse(json.dumps(data.json()))


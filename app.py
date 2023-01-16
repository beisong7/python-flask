import json
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    # if request.method == 'POST' or request.method == 'GET' :    
    
    # ts = datetime.timestamp(datetime.now())
    ts = datetime.now()
    app.logger.debug("method='{}' - path='{}' - time='{}'".format(request.method, request.path, ts))
    
    if(request.content_type != 'application/json'):
        return "<p>Hello, World!</p>"
    else:
        return json.dumps({"message":"Hello, World"})
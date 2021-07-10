from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
     app.logger.info('main request Successfull')
     return "Hello World!"

@app.route("/status")
def healthcheck():
    response =app.response_class(
        response=json.dumps({"status":"ok-healthy"}),
        status =200,
        mimetype ='application/json'
    )
    app.logger.info('status request Successfull')
    return response

@app.route("/metrics")
def metrics():
    response =app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status =200,
        mimetype ='application/json'
    )
    app.logger.info('metrics request Successfull')
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')

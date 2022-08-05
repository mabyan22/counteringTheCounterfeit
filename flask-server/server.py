from flask import Flask
import json
import os
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Members API Route
@app.route('/members')
def members():
    return {"members":["Member1","Member2","Member3"]}

@app.route('/initialNews')
@cross_origin()
def initialNews():
    print(os.listdir('.'))
    f = open('sample-response.json')
    data = json.load(f)
    f.close()
    return data

if __name__=="__main__":
    app.run(debug=True)

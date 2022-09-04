from flask import Flask
import json
import os
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/initialNews')
@cross_origin()
def initialNews():
    print(os.listdir('.'))
    from initialDataLoad import returnResults
    data = json.loads(returnResults())
    return data

@app.route('/searchQuery&query')
@cross_origin()
def searchQuery():
    print(os.listdir('.'))
    from backend import searchResults 
    data =searchResults(query)
    return data

if __name__=="__main__":
    app.run(debug=True)

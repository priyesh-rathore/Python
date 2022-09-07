# Reference : https://www.youtube.com/watch?v=-gUyWoe_SKI

from flask import Flask, jsonify
from examplejson import *

app = Flask(__name__)

@app.route('/')
def Index():
    return "Welcome to My Flask App 2."

@app.route('/examplejson/', methods=['GET'])
def get():
    return jsonify({'Users':examplejson})

@app.route('/examplejson/<int:Id>', methods=['GET'])
def getById(Id):
    return jsonify(examplejson[Id])

@app.route('/examplejson/', methods=['POST'])
def post():
    user = {'Name':'Hank', 'Id':'4', 'Role':'Police'}
    examplejson.append(user)
    return jsonify({'Created':user})
    # curl.exe -i -H "Content-Type: Application/json" -X POST http://localhost:5000/examplejson/

if __name__ == "__main__":
    app.run(debug=True)
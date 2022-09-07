from flask import Flask, request, jsonify
import requests
import json
import datetime as dt

app = Flask(__name__)

@app.route('/')
def appStart():
    mytime = (dt.datetime.now())
    return f"Flask app started. Time={mytime}"

@app.route('/fetch/')
def simple_fetch():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    output = response.json()
    json_output = {'data' : output}
    return json_output

@app.route('/request/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('requestItem')) # /request/?requestItem=<INPUT>
    ack = {'Message':f'Request recieved for {user_query}.'}
    return json.dumps(ack)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=1)
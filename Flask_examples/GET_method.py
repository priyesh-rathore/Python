from flask import Flask, json
import datetime

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello World : YT EVBS Project"

@app.route('/returninfo', methods=['GET'])
def returninfo():
    dummy_dictionary = {'1':'one', '2':'two', '3':'three', 'timestamp': datetime.datetime.now()}
    json_dump = json.dumps(dummy_dictionary)
    return json_dump

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=1)
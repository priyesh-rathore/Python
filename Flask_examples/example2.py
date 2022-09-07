from flask import Flask, json, request, jsonify
import json

# https://jsonplaceholder.typicode.com/
# http://evbs_web_express_backend_container:3002/<endpoint>

APIkey = "1b3fe4ac-35cc-444c-8b8a-f5ed2db550c9"
batteryInfo = {}
batteryIdKey = 'xyz'

AllowedActions = ['both', 'publish', 'subscribe']

app = Flask(__name__)
@app.route('/v1/ping', methods=['GET'])
def ping():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == APIkey:
        return {
                "status":200,
                "data":{
                    "message":"Rest API is running"
                }
            }
    else :
        return {
            "status":401,
            "message":"ERR-401-InvalidApiKey"
        }

@app.route('/v1/getbatteryInfo', methods=['GET','POST'])
def getbatteryInfo():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == APIkey:
        global batteryInfo
        batteryId = request.args.get('batteryId')
        data = json.loads((request.data).decode("utf-8"))
        if batteryId == batteryIdKey:
            batteryInfo["parameter1"] = data["bsuId"]
            batteryInfo["parameter2"] = data["batteryId"]
            batteryInfo["parameter3"] = data["si1"]
            batteryInfo["parameter4"] = data["si2"]
            return {
                "status":200,
                "data":batteryInfo
            }
        else:
            return {
                "status":200,
                "data":{
                    "message":"Invalid Battery ID"
                }
            }
    else :
        return {
            "status":401,
            "message":"ERR-401-InvalidApiKey"
        }
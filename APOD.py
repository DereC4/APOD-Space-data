import requests
import json

APIKEY = ""
photoJSON = ""

def helloWorld():
    print("Hello World - "+__file__)

def getAPOD():
    global photoJSON
    print(APIKEY)
    temp = requests.get("https://api.nasa.gov/planetary/apod?api_key="+APIKEY)
    temp2 = json.dumps(temp.json())
    photoJSON = json.loads(temp2)
    # print(photoJSON)
    return photoJSON

def getURL():
    global photoJSON
    # print(photoJSON)
    return photoJSON.get('url')
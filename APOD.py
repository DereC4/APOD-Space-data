import requests

def getAPOD(key):
    temp = requests.get("https://api.nasa.gov/planetary/apod?api_key={key}")
    return "WIP"
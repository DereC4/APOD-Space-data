import requests
import json
from PIL import Image
import urllib.request
import os
import random

APIKEY = ""
photoJSON = ""

def helloWorld():
    print("Hello World - "+__file__)

def getAPOD():
    global photoJSON
    print("API KEY: " + APIKEY)
    temp = requests.get("https://api.nasa.gov/planetary/apod?api_key="+APIKEY)
    temp2 = json.dumps(temp.json())
    photoJSON = json.loads(temp2)
    return photoJSON

def getDailyURL():
    global photoJSON
    getAPOD()
    return photoJSON.get('url'), photoJSON['explanation']

def loadImage(astrURL, type):
    if(type=="normal"):
        urllib.request.urlretrieve(astrURL, "tempimage.jpg")
        convert = Image.open(r"tempimage.jpg")
        convert = convert.resize((720, 480), Image.ANTIALIAS)
        convert.save(r"tempimage.png")
        os.remove("tempimage.jpg")
    elif(type=="random"):
        urllib.request.urlretrieve(astrURL, "tempimagerandom.jpg")
        convert = Image.open(r"tempimagerandom.jpg")
        convert = convert.resize((720, 480), Image.ANTIALIAS)
        convert.save(r"tempimagerandom.png")
        os.remove("tempimagerandom.jpg")
    
# Date must be between Jun 16, 1995 and {CURRENT DATE}
def getRandomURL(theAPIKey):
    '''This procedure gets a random photo URL from the NASA APOD API.
    It returns the url, as well as the date and title of the photo using an
    API key to access the database'''
    global photoJSON
    # print("API KEY: " + theAPIKey)
    tempyear = random.randint(1996, 2020)
    tempmonth = random.randint(1,12)
    tempday = random.randint(1,28)
    temp = requests.get("https://api.nasa.gov/planetary/apod?api_key="+APIKEY+"&date="+str(tempyear)+"-"+str(tempmonth)+"-"+str(tempday))  
    temp2 = json.dumps(temp.json())
    photoJSON = json.loads(temp2)
    for key in photoJSON:
        print(key.capitalize()+": "+photoJSON[key])
    if(tempmonth == 1):
        tempmonth = "January"
    elif(tempmonth == 2):
        tempmonth = "February"
    elif(tempmonth == 3):
        tempmonth = "March"
    elif(tempmonth == 4):
        tempmonth = "April"
    elif(tempmonth == 5):
        tempmonth = "May"
    elif(tempmonth == 6):
        tempmonth = "June"
    elif(tempmonth == 7):
        tempmonth = "July"
    elif(tempmonth == 8):
        tempmonth = "August"
    elif(tempmonth == 9):
        tempmonth = "September"
    elif(tempmonth == 10):
        tempmonth = "October"
    elif(tempmonth == 11):
        tempmonth = "November"
    elif(tempmonth == 12):
        tempmonth = "December"        
    return photoJSON.get('url'), tempyear, tempmonth, tempday, photoJSON["title"]

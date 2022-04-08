from re import T
import APOD
from tkinter import *
from tkinter.ttk import *
from PIL import Image
import urllib.request
import os

apikey = "03nFjsaeGH0euZf10kux3Cx1AfvidxiBxh8kWqPZ"
APOD.APIKEY = apikey
canvas = Tk()

def initCanvas():
    global canvas   
    canvas.geometry("720x480")
    canvas.title("Derek's Cool Space App")
    canvas.resizable(False, False)
    APODButton = Button(canvas,text ="Click to see the\ndaily space image!",command = loadAPODImage)
    APODButton.pack(side=LEFT, padx=15)

def loadAPODImage():
    global canvas
    # APOD.helloWorld()
    APOD.getAPOD()
    astrURL = APOD.getURL()
    urllib.request.urlretrieve(astrURL, "tempimage.jpg")
    convert = Image.open(r"tempimage.jpg")
    convert = convert.resize((720, 480), Image.ANTIALIAS)
    convert.save(r"tempimage.png")
    os.remove("tempimage.jpg")
    photoWindow = Toplevel()
    photoWindow.title("Astronomy Picture of the Day")
    canvas2 = Canvas(photoWindow, height=480, width=1080)
    photoWindow.resizable(False, False)x
    print(APOD.getURL())
    
    my_image = PhotoImage(file='tempimage.png')

    # canvas2.create_image(0, 0, anchor=NW, image=my_image)
    # canvas2.create_text(text="Image of Day")
    saveImageButton = Button(canvas2,text ="Save Image")
    saveImageButton.pack(side=RIGHT,padx=15)
    canvas2.pack()
    canvas2.mainloop()

def on_closing():
    if os.path.exists("tempimage.png"):
        os.remove("tempimage.png")
        canvas.destroy()
    else:
        canvas.destroy()    

initCanvas()
canvas.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()
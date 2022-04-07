from re import T
import APOD
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
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
    APODButton = Button(canvas,text ="Click to see the picture of the day!",command = loadAPODImage)
    APODButton.pack()



def loadAPODImage():
    global canvas
    # APOD.helloWorld()
    APOD.getAPOD()
    astrURL = APOD.getURL()
    urllib.request.urlretrieve(astrURL, "tempimage.jpg")
    convert = Image.open(r"tempimage.jpg")
    convert.save(r"tempimage.png")
    
    photoWindow = Toplevel()
    photoWindow.title("Astronomy Picture of the Day")
    canvas2 = Canvas(photoWindow, height=600, width=600)
    canvas2.pack()
    print(APOD.getURL())
    my_image = PhotoImage(file='tempimage.png')
    canvas2.create_image(0, 0, anchor=NW, image=my_image)

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
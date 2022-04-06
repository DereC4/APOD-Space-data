from re import T
import APOD
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

apikey = "03nFjsaeGH0euZf10kux3Cx1AfvidxiBxh8kWqPZ"
APOD.APIKEY = apikey
canvas = Tk()

def initCanvas():
    canvas.geometry("720x480")
    canvas.title("Derek's Cool Space App")
    canvas.resizable(False, False)
    APODButton = Button(canvas,text ="Click to see the picture of the day!",command = loadAPODImage)
    APODButton.pack()

def loadAPODImage():
    # APOD.helloWorld()
    APOD.getAPOD()
    photoWindow = Toplevel(canvas)
    photoWindow.title("Astronomy Picture of the Day")
    photoWindow.geometry("1980x1080")
    # print(APOD.getURL())
    astrURL = APOD.getURL()
    astrImage = ImageTk.PhotoImage(Image.open(astrURL))
    photoWindow.create_image(10,10,anchor=NW,image=astrImage)
initCanvas()
mainloop()
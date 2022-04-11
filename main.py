from re import T
from turtle import back
import APOD
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkhtmlview import HTMLLabel
from PIL import Image,ImageTk
import urllib.request
import os
from datetime import date

apikey = "03nFjsaeGH0euZf10kux3Cx1AfvidxiBxh8kWqPZ"
APOD.APIKEY = apikey
canvas = Tk()
todayDate = date.today()

def initApp():
    APOD.getAPOD()

def initCanvas():
    global canvas   
    canvas.geometry("1800x1000")
    canvas.title("Derek's Cool Space App")
    canvas.resizable(False, False)
    canvas.config(bg='blue')

    image1 = Image.open("awesomerenderedbackground.png")
    backgroundImage = ImageTk.PhotoImage(image1)
    backgroundLabel = tkinter.Label(canvas,image=backgroundImage)
    backgroundLabel.image = backgroundImage
    backgroundLabel.place(x=-25, y=0)
    # backgroundLabel.pack()
    APODButton = Button(canvas,text ="Click to see the\ndaily space image!",command = loadAPODImage)
    APODButton.pack(side=TOP, padx=15)
    APODButton = Button(canvas,text ="Click to see a\n random space image!",command = loadRandomAPODImage)
    APODButton.pack(side=TOP, padx=15,pady=20)
    # linktoNASA = HTMLLabel(canvas, html="""<a href = https://api.nasa.gov/index.html></a>""")
    # linktoNASA.pack(pady=20,padx=20)


def loadAPODImage():
    global canvas
    astrURL = APOD.getURL()
    APOD.loadImage(astrURL)
    print("URL: " + astrURL)

    photoWindow = Toplevel()
    photoWindow.title(("Astronomy Picture of the Day for: ",todayDate))
    photoWindow.resizable(False, False)

    canvas2 = Canvas(photoWindow, height=480, width=1080)
    my_image = PhotoImage(file='tempimage.png')
    canvas2.create_image(0, 0, anchor=NW, image=my_image)
    
    # canvas2.create_text(text="Image of Day")
    # saveImageButton = Button(canvas2,text ="Save Image")
    # saveImageButton.pack(side=RIGHT,padx=15)
    canvas2.pack()
    canvas2.mainloop()

def loadRandomAPODImage():
    global canvas
    astrURL, year, month, day = APOD.getRandomURL()
    APOD.loadImage(astrURL)
    print("URL: " +astrURL)

    photoWindow = Toplevel()
    photoWindow.title("Astronomy Picture of the Day for"+str(year)+" "+month+" "+str(day))

    canvas2 = Canvas(photoWindow, height=480, width=1080)
    photoWindow.resizable(False, False)
    my_image = PhotoImage(file='tempimage.png')

    canvas2.create_image(0, 0, anchor=NW, image=my_image)
    canvas2.pack()
    canvas2.mainloop()

def on_closing():
    if os.path.exists("tempimage.png"):
        os.remove("tempimage.png")
        canvas.destroy()
    else:
        canvas.destroy()    

initCanvas()
initApp()
canvas.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()
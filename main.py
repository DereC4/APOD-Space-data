import random
from re import T
import APOD
import tkinter
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
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
    canvas.geometry("1500x800")
    canvas.title("Cool Space App")
    canvas.resizable(False, False)
    canvas.config(bg='blue')

    backgroundImage = ImageTk.PhotoImage(Image.open("awesomerenderedbackground.png"))
    backgroundLabel = tkinter.Label(canvas,image=backgroundImage)
    backgroundLabel.image = backgroundImage
    backgroundLabel.place(x=-25, y=0)
    # backgroundLabel.pack()
    APODButton = Button(canvas,text ="Click to see the\ndaily space image!",command = loadAPODImage)
    APODButton.pack(side=TOP, padx=15,pady=10)
    APODButton2 = Button(canvas,text ="Click to see a random space image!\n(Rarely has a bad input file format; if this happens just click again)",command = loadRandomAPODImage)
    APODButton2.pack(side=TOP, padx=15,pady=10)
    # linktoNASA = HTMLLabel(canvas, html="""<a href = https://api.nasa.gov/index.html></a>""")
    # linktoNASA.pack(pady=20,padx=20)
    APODButton3 = Button(canvas,text ="Save Current Image",command = saveImage)
    APODButton3.pack(side=TOP, padx = 10, pady= 10)
    # canvas.config(menu=menubar)

def loadAPODImage():
    global canvas
    astrURL,description = APOD.getDailyURL()
    APOD.loadImage(astrURL,"normal")

    photoWindow = Toplevel()
    photoWindow.title(("Astronomy Picture of the Day for: ",todayDate))
    photoWindow.resizable(False, False)

    canvas2 = Canvas(photoWindow, height=480, width=720)
    my_image = PhotoImage(file='tempimage.png')
    canvas2.create_image(0, 0, anchor=NW, image=my_image)
    canvas2.pack()
    canvas2.mainloop()

def loadRandomAPODImage():
    global canvas
    astrURL, year, month, day, title = APOD.getRandomURL(apikey)
    APOD.loadImage(astrURL,"random")

    photoWindow = Toplevel()
    photoWindow.title(title+" taken on "+month+" "+str(day)+", "+str(year))

    canvas2 = Canvas(photoWindow, height=480, width=720)
    photoWindow.resizable(False, False)
    my_image = PhotoImage(file='tempimagerandom.png')

    canvas2.create_image(0, 0, anchor=NW, image=my_image)
    canvas2.pack()
    canvas2.mainloop()

def saveImage():
    try:
        convert = Image.open(r"tempimage.png")
        tempID = random.randint(0, 6142004)
        convert.save(r"Astronomy Photo"+str(tempID)+".png")
        print("Saved Daily Image")
    except:
        print("Failed to Save Daily Image")
    try:
        convert = Image.open(r"tempimagerandom.png")
        tempID = random.randint(0, 6142004)
        convert.save(r"Astronomy Photo"+str(tempID)+".png")
        print("Saved Random Image")
    except:
        print("Failed to Save Random Image")
        
def on_closing():
    try:
        os.remove("tempimage.png")
    except:
        pass
    try:
        os.remove("tempimagerandom.png")
    except:
        pass
    canvas.destroy()

initCanvas()
initApp()
canvas.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()
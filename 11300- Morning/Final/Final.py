# Final Project Section 2N Afternoon Class CSC113
# Mohammad Saif, Arman Uddin, Farhan Zaman
from readFile import *
from tkinter import *
from GUIChart import *

dataValue = 0
def getData(inputBox,window):
    try:
        global dataValue
        dataValue = int(inputBox.get())
        if dataValue<0:
            dataValue = 0
        window.destroy()
    except:
        popUp = Tk()
        popUpLabel = Label(popUp, text="Invalid Input")
        popUpLabel.pack()

def makeWindow():
    window = Tk()
    window.title("Final Project")
    topFrame = Frame(window)
    bottomFrame = Frame(window)
    header = Label(topFrame, text="Please enter the number of most frequent letters that you want to see")
    submitButton = Button(bottomFrame, text="Submit", command=lambda: getData(inputBox, window))
    inputBox = Entry(bottomFrame)

    topFrame.pack(side=TOP)
    bottomFrame.pack(side=BOTTOM)
    header.pack()
    submitButton.grid(row=0, column=1)
    inputBox.grid(row=0, column=0)
    window.mainloop()

makeWindow()
fileObj = readFile("Words.txt")
chartObj = GUIChart(fileObj, dataValue)
chartObj.drawChart()



from tkinter import *
from random import *
from turtle import Turtle, Screen


dataValue = 0
def getData():
    try:
        global dataValue

        dataValue = int(inputBox.get())
        window.destroy()
    except:
        popUp = Tk()
        popUpLabel = Label(popUp, text="Invalid Input")
        popUpLabel.pack()


window = Tk()
window.title("Final Project")
topFrame = Frame(window)
bottomFrame = Frame(window)
header = Label(topFrame, text="Please enter the number of most frequent letters that you want to see")
submitButton = Button(bottomFrame, text="Submit", command=getData)
inputBox = Entry(bottomFrame)

topFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)
header.pack()
submitButton.grid(row=0, column=1)
inputBox.grid(row=0, column=0)
window.mainloop()

with open("Words.txt", "r") as words:
    frequency = {}
    total = 0
    contents = words.read().lower()
    words.seek(0);
    print(words.readlines())
    for char in contents:
        total += 1
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

probabilities = {}
for key in frequency:
    probabilities[key] = (frequency[key]/total)

def extractMax():
    maxValue = 0
    maxKey = ""
    for key in probabilities:
        if probabilities[key] > maxValue:
            maxValue = probabilities[key]
            maxKey = key
    probabilities[maxKey] = 0
    return maxKey, maxValue

if dataValue > len(probabilities):
    dataValue = len(probabilities)

listMax = {}
totalProb = 0
for i in range(0, dataValue):
    maxKey, maxValue = extractMax()
    listMax[maxKey] = maxValue
    totalProb = totalProb + maxValue

totalProb = 1 - totalProb
totalProb = int(totalProb*10000)/10000
if totalProb != 0:
    listMax["All other letters"] = totalProb

colors = ['Black',
          'DarkSlateGray', 'DimGray', 'SlateGray', 'LightSlateGray', 'Gray', 'LightGray', 'MidnightBlue', 'Navy',
          'CornflowerBlue', 'DarkSlateBlue', 'SlateBlue', 'MediumSlateBlue', 'LightSlateBlue', 'MediumBlue',
          'RoyalBlue', 'Blue', 'DodgerBlue', 'DeepSkyBlue', 'SkyBlue', 'LightSkyBlue', 'SteelBlue', 'LightSteelBlue',
          'LightBlue', 'PowderBlue', 'PaleTurquoise', 'DarkTurquoise', 'MediumTurquoise', 'Turquoise', 'Cyan',
          'LightCyan', 'CadetBlue', 'MediumAquamarine', 'Aquamarine', 'DarkGreen', 'DarkOliveGreen', 'DarkSeaGreen',
          'SeaGreen', 'MediumSeaGreen', 'LightSeaGreen', 'PaleGreen', 'SpringGreen', 'LawnGreen', 'Chartreuse',
          'MediumSpringGreen', 'GreenYellow', 'LimeGreen', 'YellowGreen', 'ForestGreen', 'OliveDrab', 'DarkKhaki',
          'Khaki', 'PaleGoldenrod', 'LightGoldenrodYellow', 'LightYellow', 'Yellow', 'Gold', 'LightGoldenrod',
          'Goldenrod', 'DarkGoldenrod', 'RosyBrown', 'IndianRed', 'SaddleBrown', 'Sienna', 'Peru', 'Burlywood', 'Beige',
          'Wheat', 'SandyBrown', 'Tan', 'Chocolate', 'Firebrick', 'Brown', 'DarkSalmon', 'Salmon', 'LightSalmon',
          'Orange', 'DarkOrange', 'Coral', 'LightCoral', 'Tomato', 'OrangeRed', 'Red', 'HotPink', 'DeepPink', 'Pink',
          'LightPink', 'PaleVioletRed', 'Maroon', 'MediumVioletRed', 'VioletRed', 'Violet', 'Plum', 'Orchid',
          'MediumOrchid', 'DarkOrchid', 'DarkViolet', 'BlueViolet', 'Purple', 'MediumPurple', 'Thistle']

def getColor():
    global colors
    rand = randint(0,len(colors)-1)
    color = colors[rand]
    colors.remove(color)
    return color


radius=200
LABEL_RADIUS =radius*1.2
font_size = 18
dataValue = int(dataValue/3)
font_size = font_size - dataValue
FONT=("Ariel",font_size)

# The pie slices

baker = Turtle()
baker.penup()
baker.sety(-radius)
baker.pendown()
i=0
for key in listMax:
    actualcolor=getColor()
    baker.fillcolor(actualcolor)
    i=i+1
    baker.begin_fill()
    baker.circle(radius, listMax[key] * 360)
    position = baker.position()
    baker.goto(0, 0)
    baker.end_fill()
    baker.setposition(position)

# The labels
baker.penup()
baker.sety(-LABEL_RADIUS)

for key in listMax:
    baker.circle(LABEL_RADIUS, listMax[key] * 360 / 2)
    if key == ' ':
        baker.write("' ', "+str(int(listMax[key]*10000)/10000), align="center", font=FONT)
    elif key == '\n':
        baker.write('\\n, '+str(int(listMax[key]*10000)/10000), align="center", font=FONT)
    elif key == '\t':
        baker.write('\\t, '+str(int(listMax[key]*10000)/10000), align="center", font=FONT)
    else:
        baker.write(key + ", "+str(int(listMax[key]*10000)/10000), align="center", font=FONT)
    baker.circle(LABEL_RADIUS, listMax[key] * 360 / 2)

baker.hideturtle()

screen = Screen()
screen.exitonclick()

from readFile import *
from random import randint
from turtle import Turtle, Screen
class GUIChart():
    colors = ['Black',
              'DarkSlateGray', 'DimGray', 'SlateGray', 'LightSlateGray', 'Gray', 'LightGray', 'MidnightBlue', 'Navy',
              'CornflowerBlue', 'DarkSlateBlue', 'SlateBlue', 'MediumSlateBlue', 'LightSlateBlue', 'MediumBlue',
              'RoyalBlue', 'Blue', 'DodgerBlue', 'DeepSkyBlue', 'SkyBlue', 'LightSkyBlue', 'SteelBlue',
              'LightSteelBlue',
              'LightBlue', 'PowderBlue', 'PaleTurquoise', 'DarkTurquoise', 'MediumTurquoise', 'Turquoise', 'Cyan',
              'LightCyan', 'CadetBlue', 'MediumAquamarine', 'Aquamarine', 'DarkGreen', 'DarkOliveGreen', 'DarkSeaGreen',
              'SeaGreen', 'MediumSeaGreen', 'LightSeaGreen', 'PaleGreen', 'SpringGreen', 'LawnGreen', 'Chartreuse',
              'MediumSpringGreen', 'GreenYellow', 'LimeGreen', 'YellowGreen', 'ForestGreen', 'OliveDrab', 'DarkKhaki',
              'Khaki', 'PaleGoldenrod', 'LightGoldenrodYellow', 'LightYellow', 'Yellow', 'Gold', 'LightGoldenrod',
              'Goldenrod', 'DarkGoldenrod', 'RosyBrown', 'IndianRed', 'SaddleBrown', 'Sienna', 'Peru', 'Burlywood',
              'Beige',
              'Wheat', 'SandyBrown', 'Tan', 'Chocolate', 'Firebrick', 'Brown', 'DarkSalmon', 'Salmon', 'LightSalmon',
              'Orange', 'DarkOrange', 'Coral', 'LightCoral', 'Tomato', 'OrangeRed', 'Red', 'HotPink', 'DeepPink',
              'Pink',
              'LightPink', 'PaleVioletRed', 'Maroon', 'MediumVioletRed', 'VioletRed', 'Violet', 'Plum', 'Orchid',
              'MediumOrchid', 'DarkOrchid', 'DarkViolet', 'BlueViolet', 'Purple', 'MediumPurple', 'Thistle']
    radius = 200
    LABEL_RADIUS = radius * 1.2
    font_size = 18
    listMax = {}

    def __init__(self, fileObje, data = 0):
        self.dataValue = data
        self.fileObj = fileObje
        if self.dataValue > len(self.fileObj.probability):
            self.dataValue = len(self.fileObj.probability)

        tmpData = int(self.dataValue / 3)
        self.font_size = self.font_size - tmpData
        self.FONT = ("Ariel", self.font_size)
        self.fillListMax()


    def fillListMax(self):
        totalProb = 0
        for i in range(0, self.dataValue):
            maxKey, maxValue = self.fileObj.extractMax()
            self.listMax[maxKey] = maxValue
            totalProb = totalProb + maxValue

        totalProb = 1 - totalProb
        totalProb = int(totalProb * 10000) / 10000
        if totalProb != 0:
            self.listMax["All other letters"] = totalProb

    def getColor(self):
        rand = randint(0, len(self.colors) - 1)
        color = self.colors[rand]
        self.colors.remove(color)
        return color

    def drawChart(self):
        drawer = Turtle()
        drawer.penup()
        drawer.sety(-self.radius)
        drawer.pendown()
        i = 0
        for key in self.listMax:
            actualcolor = self.getColor()
            drawer.fillcolor(actualcolor)
            i = i + 1
            drawer.begin_fill()
            drawer.circle(self.radius, self.listMax[key] * 360)
            position = drawer.position()
            drawer.goto(0, 0)
            drawer.end_fill()
            drawer.setposition(position)

        # The labels
        drawer.penup()
        drawer.sety(-self.LABEL_RADIUS)

        for key in self.listMax:
            drawer.circle(self.LABEL_RADIUS, self.listMax[key] * 360 / 2)
            if key == ' ':
                drawer.write("' ', " + str(int(self.listMax[key] * 10000) / 10000), align="center", font=self.FONT)
            elif key == '\n':
                drawer.write('\\n, ' + str(int(self.listMax[key] * 10000) / 10000), align="center", font=self.FONT)
            elif key == '\t':
                drawer.write('\\t, ' + str(int(self.listMax[key] * 10000) / 10000), align="center", font=self.FONT)
            else:
                drawer.write(key + ", " + str(int(self.listMax[key] * 10000) / 10000), align="center", font=self.FONT)
            drawer.circle(self.LABEL_RADIUS, self.listMax[key] * 360 / 2)

        drawer.hideturtle()

        screen = Screen()
        screen.mainloop()
        #screen.exitonclick()

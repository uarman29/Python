# Arman Uddin
# Section 2N Tuesday 12:30pm - 1:45 pm

import math;

def minToMillSec():
    minutes = float(input("Please enter the number of minutes you want converted to milliseconds: "))
    milliseconds = minutes*60*1000;
    print("There are",milliseconds,"milliseconds in",minutes,"minutes")

def average():
    score1 = float(input("Please enter the first score to average: "))
    score2 = float(input("Please enter the second score to average: "))
    average = (score1+score2)/2
    print("The average is",average)

def findRoots():
    a = float(input("Please enter the coefficient of a: "))
    b = float(input("Please enter the coefficient of b: "))
    c = float(input("Please enter the coefficient of c: "))
    discrim = b*b-4*a*c
    if(a==0):
        print("No real roots")
        return;
    if(discrim<0):
        print("No real roots")
        return;
    if(discrim>=0):
        discrim = math.sqrt(b*b-4*a*c)
        root1 = (-1*b - discrim)/(2*a)
        root2 = (-1*b + discrim)/(2 * a)
        print("The roots are",root1,"and",root2)

def tempConverter():
    kelvin = float(input("Please enter a value in kelvin to be converted: "))
    r = (kelvin-273.15)*.8
    celsius = tempRtoC(r);
    print(kelvin,"degrees kelvin is",r,"degrees Reaumur and",celsius,"degrees celsius")

def tempRtoC(reaumur):
    return reaumur/.8;


def marblesIntoCube():
    side = float(input("Please enter the length of the cube: "))
    volumeC = side**3
    volumeS = (4/3)*math.pi*((side/4)**3)
    into = volumeC//volumeS
    print("You can fit",into,"marbles of radius",side/4,"into a cube of length",side)

def screenPattern():
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("i        i        i        i        i")
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")

minToMillSec(); # 3 min = 180000
average(); # The average of 80 and 93 is 86.5
findRoots(); # The roots of -20x^2+5x+5 are approximately .6403882032022076 and -.3903882032022076
tempConverter(); # 27 degrees kelvin is -196.92 degrees Reaumur and -246.15 degrees celsius
marblesIntoCube();# 15 marbles of radius 50 can fit into a cube with side 200
screenPattern();
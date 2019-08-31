# Arman Uddin
# Section 2N Tuesday 12:30pm - 1:45 pm
import math;

secondToMinutes = str(42*60);
print("There are "+secondToMinutes+" seconds in 42 minutes."); # 2520 seconds in 42 minutes

radius1 = 4;
radius2 = 6;
volume1 = str((4.0/3)*(radius1**3)*math.pi);
volume2 = str((4.0/3)*(radius2**3)*math.pi);
print("The volume of a sphere with radius 4 is "+ volume1); # 268.082573106329
print("The volume of a sphere with radius 6 is "+ volume2); # 904.7786842338604

conversion = str(-40*1.8+32);
print("-40 degrees celsius is equal to "+conversion+" degrees Fahrenheit"); # -40 degrees Fahrenheit, same thing

a = 2;
volumeR = a*2*a*3*a;
volumeC = a*a*a;
cIntoR = str(volumeR//volumeC);
print("If you have a rectangular prism with sides a,2a,3a you can fit "+cIntoR+" cubes, C with side a into R"); # 6 cubes


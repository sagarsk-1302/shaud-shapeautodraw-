# we need to install three library files
# pyaudio,speech_recognition and turtle


from models import *
import time
import turtle




print("This is a program to Draw geometrical objects using VOICE RECOGNITION")
print("SPEAK THE SHAPE TO BE DRAWN")
print("Square\nRectangle\nCircle\nTriangle\nPentagon\nHexagon\nHeptagon\nOctagon\nNonagon\nDecagon")
print("Press enter to continue: ")
input("---->")
print("Time delay of 5 seconds")
time.sleep(5)
print("you can speak in ")
shape=voice()
shape=shape.lower()
print(f"The shape that you have said is {shape}")

if "circle" in shape:
    print("Tell the radius of circle (mention pixels in multiple of 10 and pixel<=200)")
    time.sleep(2)
    radius=voice()
    print(f"the entered radius is {radius}")
    val=numconvert(radius)
    turtles=turtle.Turtle()
    turtles.color('red')
    turtles.pensize(5)
    turtles.circle(val)
    time.sleep(2)

elif "square" in shape:
    print("tell the length of sides in pixels (in the multiple of 10 and pixels<=200)")
    time.sleep(2)
    length=voice()
    print(f"the entered length is {length}")
    val=numconvert(length)
    polydraw(4,val)

elif "rectangle" in shape:
    print("tell the length of sides in pixels (in the multiple of 10 and pixels<=200)")
    time.sleep(2)
    length=voice()
    print(f"the entered length is {length}")
    leng=numconvert(length)
    print("tell the breadth of sides in pixels (in the multiple of 10 and pixels<=200)")
    time.sleep(2)
    breadth=voice()
    print(f"the entered breadth is {breadth}")
    bread=numconvert(breadth)
    turtles=turtle.Turtle()
    turtles.color('red')
    turtles.pensize(5)
    turtles.forward(leng)
    turtles.left(90)
    turtles.forward(bread)
    turtles.left(90)
    turtles.forward(leng)
    turtles.left(90)
    turtles.forward(bread)
    turtles.left(90)
    time.sleep(2)

elif ("triangle" in shape) or ("pentagon" in shape) or ("hexagon" in shape) or ("heptagon" in shape) or ("octagon" in shape) or ("nonagon" in shape) or ("decaagon" in shape):
    print(f"tell the length of {shape} in pixels (in the multiple of 10 and pixels<=200)")
    length=voice()
    print(f"the entered length is {length}")
    leng=numconvert(length)
    if "triangle" in shape:
        val=3
    elif "pentagon" in shape:
        val=5
    elif "hexagon" in shape:
        val=6
    elif "heptagon" in shape:
        val=7
    elif "octagon" in shape:
        val=8
    elif "nonagon" in shape:
        val=9
    elif "decagon" in shape:
        val=10
    else:
        print("Unknown shape")

    polydraw(val,leng)


else:
    print("shape out of my geometry :")

    




import turtle
import time
import pyaudio
import speech_recognition as sr


def value(string):
    dic={"10":10,"20":20,"30":30,"40":40,"50":50,"60":60,"70":70,"80":80,"90":90,"100":100,"110":110,"120":120,"130":130,"140":140,"150":150,"160":160,"170":170,"180":180,"190":190,"200":200,"ten":10,"twenty":20,"thirty":30,"fourty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,"hundred":100,"one ten":110,"one twenty":120,"one thirty":130,"one fourty":140,"one fifty":150,"one sixty":160,"one seventy":170,"one eighty":180,"one ninety":190,"two hundred":200}

    if dic[string]:
        return dic[string]
    else:
        return None


def voice():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
       r.adjust_for_ambient_noise(source)
       i=3
       while i>0:
           print(f"---->{i}")
           time.sleep(1)
           i-=1
       audio = r.record(source,duration=2)
    param=r.recognize_google(audio)
    time.sleep(2)
    return param

def polydraw(sides,length):
    turtles=turtle.Turtle()
    turtles.color('red')
    turtles.pensize(5)
    angle=360//sides
    for i in range(sides):
        turtles.forward(length)
        turtles.left(angle)
    time.sleep(2)



def numconvert(stringnum):
    if type(stringnum)==str:
        val=int(value(stringnum))
        if val==None:
            print("Error in handling parameter")
            exit()
        return val
    elif type(stringnum)==int:
        val=stringnum
        return val
    else:
        print("Unknown error Try again")
        exit()

from playsound import playsound
from gtts import gTTS
import os
def convey(a):

    tts = gTTS(text=a, lang='en-us')
    tts.save("hello.mp3")
    playsound("hello.mp3")
    os.remove("hello.mp3")
    print(a)

def show(a):
    input1=input("cmd:")
    if "voice" in input1:
            print(a)
    else:
            convey(a)
            

show("kabil preetham")

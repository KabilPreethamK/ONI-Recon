from playsound import playsound
from gtts import gTTS
def convey(a):
    tts = gTTS(text=a, lang='en')
    tts.save("hello.mp3")
    playsound("hello.mp3")
    
convey("how are")
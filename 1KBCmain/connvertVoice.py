from gtts import gTTS
from pygame import mixer
from playsound import playsound
import pyglet
import time, os

mixer.init()
text=[
    "Python is one of those rare languages which can claim to be both simple and powerful. "
    "You will find yourself pleasantly surprised to see how easy it is to concentrate on the "
    "solution to the problem rather than the syntax and structure of the language you are programming in."
    ]
def playmusic():
    mixer.music.load("voice.mp3")
    mixer.music.play()
def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = "voice.mp3"
    file.save(filename)
    #music = pyglet.media.load(filename)
    #music.play()
    #mixer.music.load("voice.mp3")
    #mixer.music.play()
    playsound('C:/Users/ASUS/PycharmProjects/1KBCmain/voice.mp3')
    #time.sleep(music.duration)
    #os.remove(filename)



tts(text[0],'en')

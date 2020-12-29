# every function defined here will be avaliable via speech recognition after you run build.py
from custom_commands.mycommands import *
import pyttsx3
engine = pyttsx3.init()

keyword="exec"

def hello_there():
    # print("general kenobi")
    engine.say("general kenobi")
    engine.runAndWait()
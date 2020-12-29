from custom_commands import commands
from colorama import Fore, Back, Style, Cursor
from inspect import getmembers, isfunction

functions_list = [o for o in getmembers(commands) if isfunction(o[1])]
#print(functions_list)

import speech_recognition as sr

audio_devices = sr.Microphone.list_microphone_names()
audio_device = audio_devices.index("pulse")

r = sr.Recognizer()
mic = sr.Microphone(device_index = audio_device)

def recognize_speech_from_mic():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # set up the response object
    response = {
        "transcription": None,
        "error": None
    }
    try:
        response["transcription"] = r.recognize_sphinx(audio)
    except sr.RequestError:
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def make_exec(text):
    split = text.split(" ")
    #print(split)
    if split[0] == commands.keyword:
        cmd = "_".join(split[1::])
        #print(cmd)
        for function in functions_list:
            if function[0] == cmd:
                try:
                    function[1]()
                except Exception as ex:
                    print(Fore.RED+str(ex)+Style.RESET_ALL)


def mainloop():
    while True:
        recognition=recognize_speech_from_mic()
        if recognition['transcription']:
            print(Fore.BLUE+recognition['transcription']+Style.RESET_ALL)
            make_exec(recognition['transcription'])
        elif recognition['error'] == "Unable to recognize speech":
            pass
        elif recognition['error']:
            print(Fore.RED+f"Failed because: {recognition['error']}"+Style.RESET_ALL)

mainloop()
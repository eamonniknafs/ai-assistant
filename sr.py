import speech_recognition as sr
import beepy
import os
import sys

# get audio from the microphone                                                                       
r = sr.Recognizer()

def listen():
    blockPrint()
    with sr.Microphone() as source:
        beepy.beep(1)                                                                        
        audio = r.listen(source, timeout=3)
        query = r.recognize_google(audio, language='en-US', )
        enablePrint()        
        print("You said: " + query)
        beepy.beep(1)          
        return query



# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

UnknownValueError = sr.UnknownValueError
WaitTimeoutError = sr.WaitTimeoutError
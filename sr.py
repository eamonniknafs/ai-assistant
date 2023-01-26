import speech_recognition as sr
import beepy

# get audio from the microphone                                                                       
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        beepy.beep(1)                                                                                   
        audio = r.listen(source)
        resp = r.recognize_google(audio, show_all=False, with_confidence=False, language='en-US')
        beepy.beep(1)                  
        return resp
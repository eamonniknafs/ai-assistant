import speech_recognition as sr
import beepy

# get audio from the microphone                                                                       
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        beepy.beep(1)                                                                        
        audio = r.listen(source, timeout=7)
        resp = r.recognize_google(audio, language='en-US')
        print("You said: " + resp)
        beepy.beep(1)                  
        return resp
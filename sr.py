import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()
def listen():
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)
        return r.recognize_google(audio, show_all=False, with_confidence=False, language='en-US')
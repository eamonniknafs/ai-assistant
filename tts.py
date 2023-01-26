import subprocess
import platform
import pyttsx3

def speak(text):
    if platform.system() == "Darwin":
        subprocess.call(['say', text])
    else:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

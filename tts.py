import platform

# speak text
def speak(text):
    if platform.system() == "Darwin":
        import subprocess
        subprocess.call(['say', text])
    else:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

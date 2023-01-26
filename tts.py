import subprocess

def speak(text):
    subprocess.call(['say', text])
    
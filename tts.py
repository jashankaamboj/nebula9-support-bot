import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)      # Speech speed
    engine.setProperty('volume', 1.0)    # Volume: max
    engine.say(text)
    engine.runAndWait()

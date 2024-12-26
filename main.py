import pyttsx3  # This module is help the systm to speak
import speech_recognition as sr  #This module is help to recognise the speech that user said

# Initialize the text-to-speech engine
engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('rate', 200)  # Control the speed of Jarvis voice

def speak(command):
    engine.say(command)
    engine.runAndWait()

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

try:
    print("You said: ")
    command = r.recognize_google(audio, language='en-in')
    print(command)
    engine.say(command)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An error occurred: {e}")

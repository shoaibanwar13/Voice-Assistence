import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import os
import time
import pyaudio



def sptext():
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing.....")
                data = recognizer.recognize_google(audio)
                print(data)
                return data

            except sr.UnknownValueError:
                print("Not Recognize")




def speechtxt(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.getProperty('rate')
    engine.say(x)
    engine.runAndWait()
if __name__ =='__main__':
    while True:
        #if sptext().lower() == "hey 13":
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is Molvi Londaybaz"
                speechtxt(name)
            elif "old are you" in data1:
                age = "23 year old"
                speechtxt(age)
            elif "now time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtxt(time)
            elif "badsha" in data1:
                chanal = webbrowser.open("https://youtu.be/0CvIQKz10iA")
                speechtxt(chanal)
            elif "jokes" in data1:
                jokes = pyjokes.get_jokes(language='en', category='neutral')
                print(jokes)
                speechtxt(jokes)
            elif "play song" in data1:
                add = ".\songs"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))
            elif "presentation" in data1:
                add = ".\presentations"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[0]))
            elif "exit" in data1:
                speechtxt("Thanks for using")
                break
            time.sleep(10)
















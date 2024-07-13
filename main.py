import win32com.client
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    speaker.Speak(" Welcome To Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],
                 ["facebook","https://www.facebook.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

            elif "the time" in query:
                strftime = datetime.datetime.now().strftime("%H:%M")
                speaker.Speak(f"Sir the time is {strftime}")

            elif "open camera".lower() in query.lower():
                os.system(f"open /System/Applications/Camera.app")

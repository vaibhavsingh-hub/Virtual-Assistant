# .\.venv\Scripts\Activate.ps1
# pip install speechrecognition
# pip install pyaudio
# pip install setuptools
# pip install requests
# pip install pyttsx3
# pip insatll pocketsphinx
# pip install pygame
# pip install gtts
# pip install openai
from openai import OpenAI
import  speech_recognition as sr
import pyttsx3
import webbrowser
import pyaudio
import setuptools
import requests
import musicLibrary
from gtts import gTTS
import pygame
import os
recognizer = sr.Recognizer()
# engine = pyttsx3.init()
newsapi = "News API key"

def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("voice.mp3")

def aiProcess(command):
    client = OpenAI(
    api_key  = "Your API key"
)

    completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a smart virtual assistant named Jarvis, skilled in general tasks like Alexa and Google and gives short responses."},
        {"role": "user", "content" : command}
    ]
)

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split()[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("new api link here")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article["title"])

    else:
        # let open AI handle the rquest
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Activating Jarvis...")
    # Listen for the wake word "Jarvis"
    while True:
        # obatin audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        try :
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit= 1) 
                word = r.recognize_google(audio)
                if (word.lower() == "jarvis"):
                    speak("yes")
                    # Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis active..")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
import speech_recognition as sr
from time import ctime
import webbrowser
import time

recog = sr.Recognizer()

def record_audio(ask = False): 
    with sr.Microphone() as source: 
        if ask: 
            print(ask)
        audio = recog.listen(source)
        voice_data = ''
        try: 
            voice_data = recog.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError: 
            print('Sorry, I did not understand')
        except sr.RequestError: 
            print('Sorry, my service in down')
        return voice_data

def respond(voice_data): 
    if 'what is your name' in voice_data: 
        print('My name is Suru')
    if 'what time is it' in voice_data: 
        print(ctime())
    if 'search' in voice_data: 
        search = record_audio('What do you want to search? ')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice_data: 
        location = record_audio('What location are you finding? ')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'exit' in voice_data: 
        exit()


time.sleep(1)
print('How can I help you? ')

while 1: 
    voice_data = record_audio()
    respond(voice_data)
import speech_recognition as sr
from time import ctime
import webbrowser
import time
from playsound import playsound
import os
import random
from gtts import gTTS

recog = sr.Recognizer()

def record_audio(ask = False): 
    with sr.Microphone() as source: 
        if ask: 
            suru_speaking(ask)
        audio = recog.listen(source)
        voice_data = ''
        try: 
            voice_data = recog.recognize_google(audio)
            print('User: ' + voice_data)
        except sr.UnknownValueError: 
            suru_speaking('Sorry, I did not understand')
        except sr.RequestError: 
            suru_speaking('Sorry, my service in down')
        return voice_data

def suru_speaking(audio_string): 
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data): 
    if 'what is your name' in voice_data: 
        suru_speaking('My name is Suru')
    if 'what time is it' in voice_data: 
        suru_speaking(ctime())
    if 'search' in voice_data: 
        search = record_audio('What do you want to search? ')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        suru_speaking('Here is what I found for ' + search)
    if 'find location' in voice_data: 
        location = record_audio('What location are you finding? ')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        suru_speaking('Here is the location of ' + location)
    if 'exit' in voice_data: 
        exit()


time.sleep(1)
suru_speaking('How can I help you? ')

while 1: 
    voice_data = record_audio()
    respond(voice_data)
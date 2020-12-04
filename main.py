import speech_recognition as sr

recog = sr.Recognizer()

def record_audio(): 
    with sr.Microphone() as source: 
        audio = recog.listen(source)
        voice_data = ''
        try: 
            voice_data = recog.recognize_google(audio)
        except sr.UnknownValueError: 
            print('Sorry, I did not understand')
        except sr.RequestError: 
            print('Sorry, my service in down')
        return voice_data

def respond(voice_data): 
    if 'what is your name' in voice_data: 
        print('My name is Suru')


print('How can I help you? ')

voice_data = record_audio()
respond(voice_data)
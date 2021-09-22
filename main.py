"""
import scope
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
# here we create a recognizer to recognize our voice
"""
here we use our mic as a source of   audio/voice and use speech recognition to 
"""

listener = sr.Recognizer()
engine = pyttsx3.init()
# changing to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone()as source:
            engine.say('how can i help you')
            print('listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                engine.say('you should call me by my given name')
    except:
        pass
    return command


def run_alexa():

    command = take_command()
    # play song from youtube
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    # telling time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is:'+time)
    # find the person er want
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    # for fun
    elif 'data' in command:
        talk('sorry,im a robot ')
    # tells random joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('please say the command')


while True:
    run_alexa()
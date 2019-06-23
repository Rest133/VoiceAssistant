import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import pywin32_system32


def talk(words):
    print(words)

    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1

        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + task)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command()
    return task


def make_something(task):
    if "открой сайт" in task:
        talk("Уже открываю")
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'стоп' in task:
        talk("Уже выполняю")
        sys.exit()

while True:
    make_something(command())


talk("Привет, спроси у меня что-либо")

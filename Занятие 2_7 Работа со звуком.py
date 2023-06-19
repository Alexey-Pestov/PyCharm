# import os
# import time
#
# from gtts import gTTS
# from pygame import mixer
#
# my_file = open('sound.txt', 'r', encoding='utf-8')
# my_text = my_file.read()
# my_file.close()
#
# mixer.init()
# tts = gTTS(text=my_text, lang='en')
# tts.save('sound.mp3')
# mixer.music.load('sound.mp3')
# mixer.music.play()
# while mixer.music.get_busy():
#     time.sleep(1)
# mixer.music.unload()

import pyaudio
import speech_recognition as sr

recognize = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print('\nГоворите')
        audio = recognize.listen(source)
    speech = recognize.recognize_google(audio, language='ru_RU').lower()
    print('Вы сказали: ', speech)

    if speech == 'привет':
        print('Ну, здравствуй')
    if speech == 'пока':
        print('До свидания')
        break
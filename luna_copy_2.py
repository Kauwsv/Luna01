import speech_recognition as sr
from gtts import gTTS
import random
import webbrowser
import pygame
import os

class VirtualAssistant:
    def __init__(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name
        self.recognizer = sr.Recognizer()

    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                print('Ouvindo...')
                self.engine_speak(ask)

            audio = self.recognizer.listen(source, 5, 5)
            print('Processando dados de entrada...')
            try:
                voice_data = self.recognizer.recognize_google(audio, language='pt-BR')
            except sr.UnknownValueError:
                self.engine_speak('Desculpe Chefe, não entendi o que você disse. Você pode, por favor, repetir?')
                voice_data = ""
            except sr.RequestError:
                self.engine_speak('Desculpe Chefe, meu servidor está fora do ar')
                voice_data = ""

            print(">>", voice_data.lower())
            return voice_data.lower()

    def engine_speak(self, audio_string):
        tts = gTTS(text=audio_string, lang='pt')
        audio_file = 'audio.mp3'
        tts.save(audio_file)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
        pygame.quit()

        print(self.assist_name + ':', audio_string)

        os.remove(audio_file)

    def respond(self, voice_data):
        if any(phrase in voice_data for phrase in ['oi', 'olá', 'hey', 'hi', 'hello', 'fala']):
            greetings = [
                f'Olá {self.person}, o que vamos fazer hoje?',
                'Oi Chefe, como posso ajudar?',
                'Olá Chefe, do que você precisa?'
            ]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            self.engine_speak(greet)

        if 'pesquise por' in voice_data and 'youtube' not in voice_data:
            search_term = voice_data.split("por")[-1]
            url = "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para " + search_term + ' no Google')

        if 'pesquise no youtube por' in voice_data:
            search_term = voice_data.split("por")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para " + search_term + ' no YouTube')

        if 'open sap' in voice_data:
            pass


assistant = VirtualAssistant('Luna', 'Kauane')

while True:
    voice_data = assistant.record_audio('Ouvindo...')
    assistant.respond(voice_data)

    if any(exit_phrase in voice_data for exit_phrase in ['tchau', 'até logo', 'adeus', 'bye bye', 'bye', 'see you']):
        assistant.engine_speak("Tenha um bom dia! Até logo!")
        break
import speech_recognition as sr
from gtts import gTTS
import random
import webbrowser
import pygame
import os

class VirtualAssistant:
    def __init__(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name
        self.recognizer = sr.Recognizer()

    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                print('Ouvindo...')
                self.engine_speak(ask)

            audio = self.recognizer.listen(source, 5, 5)
            print('Processando dados de entrada...')
            try:
                voice_data = self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                self.engine_speak('Desculpe Chefe, não entendi o que você disse. Você pode, por favor, repetir?')
                voice_data = ""
            except sr.RequestError:
                self.engine_speak('Desculpe Chefe, meu servidor está fora do ar')
                voice_data = ""

            print(">>", voice_data.lower())
            return voice_data.lower()

    def engine_speak(self, audio_string):
        tts = gTTS(text=audio_string, lang='pt')
        audio_file = 'audio.mp3'
        tts.save(audio_file)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
        pygame.quit()

        print(self.assist_name + ':', audio_string)

        os.remove(audio_file)

    def respond(self, voice_data):
        if any(phrase in voice_data for phrase in ['oi', 'olá', 'hey', 'hi', 'hello', 'fala']):
            greetings = [
                f'Olá {self.person}, o que vamos fazer hoje?',
                'Oi Chefe, como posso ajudar?',
                'Olá Chefe, do que você precisa?'
            ]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            self.engine_speak(greet)

        if 'pesquise por' in voice_data and 'youtube' not in voice_data:
            search_term = voice_data.split("por")[-1]
            url = "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para " + search_term + ' no Google')

        if 'pesquise no youtube por' in voice_data:
            search_term = voice_data.split("por")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para " + search_term + ' no YouTube')

        if 'open sap' in voice_data:
            pass


assistant = VirtualAssistant('Luna', 'Kauane')

while True:
    voice_data = assistant.record_audio('Ouvindo...')
    assistant.respond(voice_data)

    if any(exit_phrase in voice_data for exit_phrase in ['tchau', 'até logo', 'adeus', 'bye-bye', 'bye', 'see you']):
        assistant.engine_speak("Tenha um bom dia! Até logo!")
        break

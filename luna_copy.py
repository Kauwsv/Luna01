import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import mediainfo
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os

AudioSegment.ffmpeg = "C:/Users/user/Downloads/ffmpeg-6.1/ffmpeg-6.1/fftools/ffmpeg"
mediainfo.ffmpeg = "C:/Users/user/Downloads/ffmpeg-6.1/ffmpeg-6.1/fftools/ffmpeg"

class Virtual_assit():
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()

        self.voice_data = ''

    def engine_speak(self, text):
        """
        fala da assitente virtual
        """
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def record_audio(self, ask=""):

        with sr.Microphone() as source:
            if ask:
                print('Ouvindo...')
                self.engine_speak(ask)

            audio = self.r.listen(source,5 , 5)# pega dados de auido
            print('Processando dados de entrada...')
            try:
                self.voice_data = self.r.recognize_google(audio) #converte audio para texto

            except sr.UnknownValueError:
                self.engine_speak('Desculpe Chefe, não entendi o que você disse. Você pode, por favor, repetir?')

            except sr.RequestError:
                self.engine_speak('Desculpe Chefe, meu servidor está fora do ar') # recognizer is not connected

            print(">>",self.voice_data.lower()) #imprime o que vc disse
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='pt')
        r = random.randint(1,20000)
        audio_file = 'audio' + str(r) + '.mp3'
        
        print("Diretório atual:", os.getcwd())
        
        tts.save(audio_file)
        
        sound = AudioSegment.from_file(audio_file, format="mp3")
        play(sound)
        
        print(self.assit_name + ':', audio_strig)
        os.remove(audio_file)


    def there_exist(self, terms):
        """
        função para identificar se o termo existe
        """
        for term in terms:
            if term in self.voice_data:
                return True


    def respond(self, voice_data):
        if self.there_exist(['oi', 'olá', 'hey', 'hi', 'hello', 'fala']):
            greetigns = [f'Olá {self.person}, o que vamos fazer hoje?',
                        'Oi Chefe, como posso ajudar?',
                        'Olá Chefe, do que você precisa?']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)

        #google
        if self.there_exist(['pesquise por']) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url =  "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para " + search_term + 'no google')

        #google 
        if self.there_exist(["pesquise no youtube por"]):
            search_term  = voice_data.split("for")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para" + search_term + 'no youtube')

        #spa
        if self.there_exist(['open sap']):
            pass


assistent = Virtual_assit('Luna', 'Kauane')

while True:

    voice_data = assistent.record_audio('Ouvindo...')
    assistent.respond(voice_data)

    if assistent.there_exist(['tchau', 'até logo', 'adeus', 'bye bye', 'bye', 'see you']):
        assistent.engine_speak("Tenha um bom dia! Até logo!")
        break
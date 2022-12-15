from datetime import datetime
import pyttsx3
import speech_recognition as sr
import pyaudio
import time
import os
import wikipedia
import pyautogui as pg
#import pocketsphinx


#Funções
def open_chrome() :
    os.system("start Chrome.exe")
    time.sleep(0.5)
    pg.hotkey('win', 'up')

def open_tt() :
    open_chrome()
    time.sleep(1)
    pg.write('twitter.com')
    time.sleep(0.5)
    pg.press('enter')



#Propriedades de fala
en = pyttsx3.init()
en.setProperty('rate', 182)
en.setProperty('volume', 0.8)
en.setProperty('voice', b'brazil')

def talk(self) :
    en.say(self)
    en.runAndWait()

#Talks
ouvindo = "Estou ouvindo, pode dizer"
ola = "olá, em que posso ajudar?"
ex = "Estou executando, só um minuto."
conc = "Tarefa concluída com sucesso. Deseja mais alguma coisa?"

    

#Reconhecimento de fala
def reconhecimento() :
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source, duration=3) 
        print ('Ouvindo...')
        audio = recon.listen(source)
    try:
        frase = recon.recognize_google(audio,language='pt-BR')
        frase = frase.lower()

        if "house" in frase :
            talk(ouvindo)

        if "ola" in frase:
            talk(ola)

        if "navegador" in frase:
            open_chrome()

        if "twitter" in frase:
            open_tt()
            talk(conc)

 
        if "fale sobre" in frase:
            procurar = frase.replace('fale sobre', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            print(resultado)
            talk(resultado)
            
        

    except sr.UnknownValueError:
        print("Não entendi.")




talk(ola)
while True :
    reconhecimento()

        
        

        







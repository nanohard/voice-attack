#!/usr/bin/python
import os
import time
import speech_recognition as sr

#audio playback
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125)

#allows keyboard emulation
from pynput.keyboard import Key, Controller
keyboard = Controller()

#function to read text out loud
def pySay(text):
     engine.say(text)
     engine.runAndWait()

#built in functions.
def vA():
    pySay("Voice attack sucks, free programs are better!")

def creator():
    #l33tlinuxh4x0r phoneticly spelled out.
    pySay('I was created by leet linux haxor also known as Linux.')

#player macros
def landingGear():
    keyboard.press('l')
    keyboard.release('l')

def nightVision():
    keyboard.press('n')
    keyboard.release('n')
    pySay('Toggling night vision.')
    
def shipLights():
    keyboard.press('f')
    keyboard.release('f')
    pySay('Toggeling ship lights')

def optimalSpeed():
    keyboard.press(Key.f7)
    keyboard.release(Key.f7)

def galaxyMap():
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)

def systemMap():
    keyboard.press(Key.f6)
    keyboard.release(Key.f6)

def shipStop():
    keyboard.press('x')
    keyboard.release('x')

def resetPips():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    pySay('Pips reset.')
    
def shields():
    resetPips()
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.1)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.1)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    pySay('All pips to shields.')

def engines():
    resetPips()
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(0.1)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(0.1)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    pySay('All pips to engines.')

def weapons():
    resetPips()
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.1)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.1)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    pySay('All pips to weapons.')

def superBoost():
    resetPips()
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.1)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(0.1)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(0.1)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(0.1)
    keyboard.press(Key.f10)
    keyboard.release(Key.f10)
    time.sleep(0.1)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
    time.sleep(6)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
    time.sleep(6)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)

def fsd():
    keyboard.press('j')
    keyboard.release('j')

def cargoScoop():
    keyboard.press(Key.home)
    keyboard.release(Key.home)

def micToggle():
    keyboard.press('\\')
    keyboard.release('\\')
    keyboard.press(Key.scroll_lock)
    keyboard.release(Key.scroll_lock)
    pySay('Toggling mic.')

#triggers...
macroTrigger = {
    vA: ['voice attack'],
    landingGear: ['landing gear', 'toggle landing gear'],
    nightVision: ['night vision', 'toggle night vision'],
    shipLights: ['toggle ship lights', 'battleship lights'],
    optimalSpeed: ['optimal speed', 'seventy five percent', '75%'],
    galaxyMap: ['open galaxy map'],
    systemMap: ['open system map'],
    shipStop: ['stop ship', 'slow the fuck down', 'slow the f*** down'],
    superBoost: ['superboost', 'super boost', 'get the fuck out of here', 'get the f*** out of here'],
    resetPips: ['reset pips', 'reset tips', 'recept tips'],
    shields: ['all pips to shields', 'full shields', 'full systems', 'four shields', 'four systems'],
    engines: ['all pips to engines', 'full engines', 'pull engines', 'four engines'],
    weapons: ['all pips to weapons', 'full weapons', 'pull weapons', 'four weapons'],
    fsd: ['frameshift', 'safe disengage'],
    cargoScoop: ['cargo scoop'],
    micToggle: ['toggle mic', 'toggle mike', 'taco mike', 'brb', 'be right back', 'i\'ll be back'],
    creator: ['who made you?', 'who made you'],
    }


def main():
    #infinite loop
    while True:
        #initialize a list that will be sorted later for commands
        listOrder = []
        #speech recognition initialization
        r = sr.Recognizer()
        r.pause_threshold = 0.5
        m = sr.Microphone()
        with m as source:
            try:
                audio = r.listen(source, timeout = 1.0)
                voiceInput = r.recognize_google(audio)
                print(voiceInput)

                #a method to make commands and triggers universal so it can just be called instead of using a bunch of ifs
                def queueMacro(command, keywords):
                    #if any(text in voiceInput.lower() for text in keywords):
                    for text in keywords:
                        if text in voiceInput.lower():
                            pos = voiceInput.find(text)
                            listOrder.append([pos, command])
                  
                #each command and its triggers
                for command, trigger in macroTrigger.items():
                    queueMacro(command, trigger)          
                
            #error handling for speech recognition                 
            except sr.UnknownValueError:
                print("Google could not understand audio")
            except sr.RequestError as e:
                print("Google error; {0}".format(e))
            except sr.WaitTimeoutError:
                print("No audio detected")
        
        #sort commands in order of them being triggered and run them.
        listOrder.sort(key=lambda r:r[0])
        for pos, command in listOrder[:]:
            command()
main()

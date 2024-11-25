import pyttsx3
import tkinter as tk
from playsound import playsound
from termcolor import colored
from colorama import init
import os
from To Do List import *
init()
engine=pyttsx3.init()
engine.setProperty('rate',180)
def tts(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def print_colored(text, color="white", on_color=None, attrs=None):
    print(colored(text, color=color, on_color=on_color, attrs=attrs))

def explain_module(name):
    pass
def print_colored(text, color="white", on_color=None, attrs=None):
    print(colored(text, color=color, on_color=on_color, attrs=attrs))

def tts_commands():
    tts('choose one of the options given below')

    tts('1. read the text\n\
2.give audio file of given text')
    inpt=input('enter your chice..(1,2,..)')
    if inpt=='1':
        inp=input('enter the you want to listen from me..')
        print('Your Text Is..')
        tts(inp)
    elif inpt=='2':
        inp=input('enter the text you wanna convert to an audio file')
        engine.say('enter the name of the audio file')
        f_name=input('enter..(eg;file.mp3)')
        print("Your Text Is..")
        
        engine.save_to_file(inp,f_name)
        print(inp)
        playsound(f_name)
def starting():
    print_colored('hello sir Welcome! \nI am Chanakya , \nI am under making process',color='green')
    engine.say('hello sir Welcome! i am chanakya')
    engine.runAndWait()        
if __name__=='__main__':
    starting()


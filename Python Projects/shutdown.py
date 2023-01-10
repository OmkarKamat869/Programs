# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:43:54 2021

@author: Omkar  Kamat
"""

import os
import pyttsx3
import speech_recognition as sr

#Creating class
class pythonhub:
    #Mention to take voice command as input
    def takeCommands(self):
        #Using Recognizer and microphone method for input voice
        # commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            #Number of seconds of non-speaking audio before
            #a phrase is considered complete
            r.pause_threshold = 0.7
            audio = r.listen(source)
            #Voice input is identified
            try:
                #Listening voice commands in Indian english
                print("Recognizing")
                Query = r.recognize_google(audio, language='en-in')
                
                #Displaying te voice command
                print("the query is printed='", Query, "'")
            except Execution as e:
                #Displaying exception 
                print(e)
                #Handling exception
                print("Say that again sir")
                return "None"
        return Query
    #Method for voice input
    def Speak(self, audio):
        
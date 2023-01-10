# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:53:04 2021

@author: Omkar  Kamat
"""

# Importing required modules
import os
import speech_recognition as sr
import pyttsx3


# Creating class
class Gfg:
	
	# Method to take coice commands as input
	def takeCommands(self):
		
		# Using Recognizer and Microphone Method for input voice commands
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening')

			# Number pf seconds of non-speaking audio before
			# a phrase is considered complete
			r.pause_threshold = 0.7
			audio = r.listen(source)

			# Voice input is identified
			try:

				# Listening voice commands in indian english
				print("Recognizing")
				Query = r.recognize_google(audio, language='en-in')

				# Displaying the voice command
				print("the query is printed='", Query, "'")

			except Exception as e:

				# Displaying exception
				print(e)
				# Handling exception
				print("Say that again sir")
				return "None"
		return Query

	
	# Method for voice output
	def Speak(self, audio):
	
		# Constructor call for pyttsx3.init()
		engine = pyttsx3.init('sapi5')

		# Setting voice type and id
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		engine.say(audio)
		engine.runAndWait()

	
	# Method to self shut down system
	def quitSelf(self):
		self.Speak("what is my order omkar")

		# Input voice command
		take = self.takeCommand()
		choice = take
		if choice == 'shutdown the lap baby':

			# Shutting down
			print("Shutting down the computer")
			self.Speak("Shutting the computer")
			os.system("shutdown /s /t 30")
		if choice == 'no':

			# Idle
			print("Thank u sir")
			self.Speak("Thank u sir")

			

# Driver code			
if __name__ == '__main__':
	Maam = Gfg()
	Maam.quitSelf()
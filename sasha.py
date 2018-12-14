import speech_recognition as sr
import os
import time 
import webbrowser
import winspeech 
import pygame
from pygame import mixer
import sys
from modules import checkEmail
sys.path.append("C:/Users/cody/Desktop/test/modules")
from checkEmail import openEmail
def talk(audio):
	winspeech.say(audio)
	
def listenForCmd():

	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print("Hello. i am SASHA. i'm online and ready")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)
		
	try:
		command = r.recognize_google(audio).lower()
		print("Your command:", command)
	
	except sr.UnknownValueError:
		print("the mic isnt working right... i didnt hear any command")
		command = listenForCmd()
		
	return command
#The pitch was controlled by the freqency argument in mixer.init(). So I just set that higher

def cmd(command): #function for playing user's commands
	
	if "what up" in command:
		mixer.init()
		mixer.music.load("C:/Users/cody/Desktop/test/sounds/Bidding.mp3")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(10)


	elif "defeated by victory" in command:
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/cody/Desktop/test/sounds/defeated_by_victory.ogg")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(10)

		
	elif "shakespeare" in command:
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/cody/Desktop/test/sounds/shakespeare (1).ogg")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(13)
		
		
	elif "you're weird" in command:
		mixer.init()
		mixer.music.load("C:/Users/cody/Desktop/test/eatmyshorts.wav")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(1)

	elif 'listen here' in command: 
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/cody/Desktop/test/sounds/listening.mp3")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(1)
		
	elif 'check my email' in command:
		talk("opening email")
		checkEmail.openEmail()
		
	elif 'victory' in command: 
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/cody/Desktop/test/sounds/yay.mp3")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.wait(5)

	mixer.quit()


talk("ready when you are")

while True:
	cmd(listenForCmd())
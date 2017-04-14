from math import *
from random import *
seed()
import Monster as mon
import Action as act
import Player as pc
import numpy as np
import os


#Woo, let's-a go!
class Main:
	def __init__(self):
		self.player = pc.Player
		self.mon = mon.Monster
		
class Char():
	def __init__(self):
		self.player = pc.Player()

	#Check for player data
	if os.path.exists("charStats.npy"):
		print("Character loaded!")	#Feedback for loaded character
		charStats = np.load("charStats.npy")
		playerName = charStats[0]
		playerHealth = charStats[1]				#THESE ARE
		playerMana = charStats[2]				#THE LOADED
		playerSpeed = charStats[3]				#STATS, DO
		playerExp = charStats[4]				#NOT TRY
		playerLocation = charStats[5]			#TO RELOAD
	#New player if data does not exist
	else:
		playerName = input("What is your name brave adventurer?\n")
		playerHealth = 20
		playerMana = 0
		playerSpeed = 7
		playerExp = 0
		playerLocation = None
		charStats = np.array([playerName, playerHealth, playerMana, playerSpeed, playerExp, playerLocation])
		np.save("charStats.npy", charStats)
		
	print(charStats)	#Debugging print statement
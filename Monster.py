import Action as act
from random import *
seed()

class Monster:
	def __init__(self):
		self.health = None
		self.mana = None
		self.speed = None
		self.dmgRange = []
		
	def attack(self):
		act.attack(self.speed, self.dmgRange)

###		
class Gel(Monster):
	def __init__(self):
		self.health = randint(4, 7)
		self.mana = 0
		self.speed = randint(1, 3)
		self.dmgRange = [2, 4]

###		
class Float_Gel(Monster):
	def __init__(self):
		self.health = randint(2, 5)
		self.mana = randint(2, 8)
		self.speed = randint(3, 5)
		self.dmgRange = [1, 3]
		

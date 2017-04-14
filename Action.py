from random import *

#Attack action
def attack(speed, dmgRange):
	percentSpeed = random() + (speed / 100)
	if percentSpeed >= 0.9:	#If crit hit occurs
		print("Critical!")
		dmg = str(int(round(dmgRange[1] * choice([2, 2.5]), 0)))
		#Yes, this is spaghetti code. Yes, this is probably a really inefficient way of doing it.
		#If you're so high and mighty to judge it, you fix it, jerk.
		print("Did " + dmg + " damage!")
	elif percentSpeed <= 0.1:
		print("Complete miss!")	#If a miss occurs
		dmg = str(0)
		print("Did " + dmg + " damage!")
	else:	#If a regular hit occurs
		bot = dmgRange[0]
		top = dmgRange[1]
		dmg = str(randint(bot, top))
		print("Did " + dmg + " damage!")
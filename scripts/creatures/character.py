#class for character for text-based game
#the character class is used for the player-controlled character
#wheras the creature class can be used to refer to both player-controlled
#and non-player characters

from creature import *

class Character(Creature):
	def __init__(self, pName, pHealth, pStrength):
		super(Character, self).__init__(pName, pHealth, pStrength)
	def moveTo(self, newRoom): #override from Creature
		self.room.playerExits()
		self.room = newRoom
		self.room.playerEnters()

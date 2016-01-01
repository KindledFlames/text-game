#class for character for text-based game

from creature import *

class Character(Creature):
	def __init__(self, pName, pHealth, pStrength):
		super(Character, self).__init__(pName, pHealth, pStrength)
	def moveTo(self, newRoom): #override from Creature
		self.room.playerExits()
		self.room = newRoom
		self.room.playerEnters()

#class for character for text-based game
#the character class is used for the player-controlled character
#wheras the creature class can be used to refer to both player-controlled
#and non-player characters

from creature import *

class Character(Creature):
	def __init__(self, pName, pHealth, pStrength, dexterity=5, intelligence=5, items=[], weapons=[], room=None, level=1, experience=0):
		self.level = level
		self.experience = experience
		super(Character, self).__init__(pName, pHealth, pStrength)
	def moveTo(self, newRoom): #override from Creature
		if None!=self.room:
			self.room.playerExits()
		newRoom.addCreature(self)
		self.room.playerEnters()
	def addExperience(self, exp): #add experience points
		self.experience += exp
		self.checkIfLevelUp()
	def checkIfLevelUp(self): #if experience is above a threshold, level the character up and increase stats
		if experience >= level*level*10:
			self.levelUp()
	def levelUp(self):
		#Note: later I imagine we'll want to implement a more complex leveling system. For now, I'm just having leveling increase stats in general
		self.experience -= level*level*10
		self.level += 1
		self.strength += 1
		self.dexterity += 1
		self.intelligence += 1
		self.health += 2

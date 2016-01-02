#creature class
#creatures refer to any kind of autonomous being, both player and non-player
#controlled

class Creature(object):
	#simple constructor for creature
	def __init__(self, name="DEFAULT", health=4, strength=5, dexterity=5, intelligence=5, items=[], weapons=[], room=None):
		self.name = name
		self.maxHealth = health
		self.health = health
		self.strength = strength
		self.dexterity = dexterity
		self.intelligence = intelligence
		self.items = items
		self.weapons = weapons
		self.room = room
	def checkIfDead(self): #method to check if creature is dead and to kill character if they are dead
		if self.health<=0:
			self.die()
	def takeDamage(self, damage): #reduces the creature's health by a given amount and checks if dead
		self.health -= damage
		self.checkIfDead()
	def healDamage(self, damageHealed): #heals creature by the given amount. Creatures can only heal up to max health
		self.health = min(self.maxHealth, self.health+damageHealed)
	def __str__(self): #overrides the str method for the Creature class
		return self.name+"\nHealth: "+ str(self.health)+"\nStrength: "+ str(self.strength)
	def getStat(self, statName): #gets the "str", "dex", or "int" stat
		if statName == "str":
			return self.strength
		elif statName == "dex":
			return self.dexterity
		elif statName == "int":
			return self.intelligence
	def addWeapon(self, weapon): #add weapon to the creature's weapon list
		self.weapons.append(weapon)
	def die(self): #kills the character
		print self.name, "is dead"
	def moveTo(self, newRoom): #set the creatures room to the given room
		self.room = newRoom

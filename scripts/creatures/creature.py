#creature class

class Creature(object):
	def __init__(self, name, health, strength, dexterity, intelligence, items=[], weapons=[]):
		self.name = name
		self.maxHealth = health
		self.health = health
		self.strength = strength
		self.dexterity = dexterity
		self.intelligence = intelligence
		self.items = items
		self.weapons = weapons
	def takeDamage(self, damage):
		self.health -= damage
	def healDamage(self, damageHealed):
		self.health = min(self.maxHealth, self.health+damageHealed)
	def __str__(self):
		return self.name+"\nHealth: "+ str(self.health)+"\nStrength: "+ str(self.strength)
	def getStat(self, statName):
		if statName == "str":
			return self.strength
		elif statName == "dex":
			return self.dexterity
		elif statName == "int":
			return self.intelligence
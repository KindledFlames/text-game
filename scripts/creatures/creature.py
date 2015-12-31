#creature class

class Creature(object):
	def __init__(self, name, health, strength):
		self.name = name
		self.maxHealth = health
		self.health = health
		self.strength = strength
	def takeDamage(self, damage):
		self.health -= damage
	def healDamage(self, damageHealed):
		self.health = min(self.maxHealth, self.health+damageHealed)
	def __str__(self):
		return self.name+"\nHealth: "+ str(self.health)+"\nStrength: "+ str(self.strength)
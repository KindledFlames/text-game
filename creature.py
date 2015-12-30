#creature class

class Creature(object):
	def __init__(self, health, strength):
		self.maxHealth = health
		self.health = health
		self.strength = strength
	def takeDamage(self, damage):
		self.health -= damage
	def healDamage(self, damageHealed):
		self.health = min(self.maxHealth, self.health+damageHealed)
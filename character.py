#class for character for text-based game

class Character(object):
	def __init__(self,health):
		self.maxPHealth = health
		self.pHealth = health
	def takeDamage(self,damage):
		self.pHealth -= damage
	def healDamage(self,damageHealed):
		self.pHealth = min(self.maxPHealth,self.pHealth+damageHealed)
	
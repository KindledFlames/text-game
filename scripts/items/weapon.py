#weapon class subclass of item

from item import *
import random

class Weapon(Item):
	def __init__(self, name, weight, number, accuracy, damage, critRate, critMultiplier, requiredStatAmount, requiredStatType):
		super(Weapon, self).__init__(name, weight, number)
		self.accuracy = accuracy
		self.damage = damage
		self.critRate = critRate
		self.critMultiplier = critMultiplier
		self.requiredStatAmount = requiredStatAmount
		self.requiredStatType = requiredStatType
	def attack(self, usedBy, usedOn):
		damageMultiplier = 1
		statDifference = usedBy.getStat(requiredStatType) - requiredStatAmount
		if (random.randint(1,100)+min(5, statDifference)<=accuracy):
			if (random.randint(1,100)+min(5, statDifference):
				damageMultiplier = self.critMultiplier
			usedOn.takeDamage(int(self.damage+min(5, statDifference)))
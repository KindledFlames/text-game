#weapon class subclass of item

#weapons can be used by creatures to attack other creatures and lower their health
#
#all weapons require a certain creature stat to use (e.g. strength or "str")
#when the creature has below the required stat, the weapon will be weaker and less accurate
#when the creature has above the required stat, the converse is true, though the weapon can only be 5 points better than it naturally is

from item import *
import random

class Weapon(Item):
	def __init__(self, name, weight, number, accuracy, damage, critRate, critMultiplier, requiredStatAmount, requiredStatType):
		super(Weapon, self).__init__(name, weight, number)
		self.accuracy = accuracy #percent accuracy
		self.damage = damage #number of damage points the weapon does
		self.critRate = critRate #probability of getting a critical hit
		self.critMultiplier = critMultiplier #amount by which damage is multiplied when a critical has been got
		self.requiredStatAmount = requiredStatAmount #amount of required stat the creature must have for the weapon to perform normally
		self.requiredStatType = requiredStatType #the stat required for the creature to use the weapon
	def attack(self, usedBy, usedOn):
		damageMultiplier = 1 #amount by which the damage is multiplied. 1 unless a critical hit happens
		statDifference = usedBy.getStat(self.requiredStatType) - self.requiredStatAmount #the amount by which the character's stat exceeds the weapon's required stat
		if (random.randint(1,100)+min(5, statDifference)<=self.accuracy): #roll to hit
			if (random.randint(1,100)+min(5, statDifference)<=self.critRate): #roll to crit
				damageMultiplier = self.critMultiplier
			damageToDeal = int(damageMultiplier * max(self.damage+min(5, statDifference),0))
			usedOn.takeDamage(damageToDeal) 



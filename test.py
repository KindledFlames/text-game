#test file to test character class

from scripts.creatures.creature import *
from scripts.creatures.character import *
from scripts.items.item import *

"""
testcharacter = Character(4, 5)
print "Health:", testcharacter.health
print "Strength:", testcharacter.strength
print "-2 hp"
testcharacter.takeDamage(2)
print "Health:", testcharacter.health
print "+3 hp"
"""

testitem = Item('Rock', 3)
print str(testitem)
print testitem.fullName()
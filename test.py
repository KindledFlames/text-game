#test file to test character class

from scripts.creatures.creature import *
from scripts.creatures.character import *

testcharacter = Character("Rathtar", 4, 5)
print "Health:", testcharacter.health
print "Strength:", testcharacter.strength
print "-2 hp"
testcharacter.takeDamage(2)
print "Health:", testcharacter.health
print "+3 hp"
testcharacter.healDamage(3)
print "Health:", testcharacter.health

print str(testcharacter)
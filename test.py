#test file to test character class

from scripts.creatures.creature import *
from scripts.creatures.character import *
from scripts.items.item import *
from scripts.items.weapon import *
from scripts.rooms.room import *

testCharacter = Character("Bob", 4, 5)
testMonster = Creature("Manster", 3, 3)
testRoom1 = Room([testCharacter, testMonster], 1, True)
testRoom2 = Room([], 2)
"""
print "Health:", testcharacter.health
print "Strength:", testcharacter.strength
print "-2 hp"
testcharacter.takeDamage(2)
print "Health:", testcharacter.health
print "+3 hp"

testitem = Item('Rock', 3)
print str(testitem)
print testitem.fullName()
"""
print "Character\n", testCharacter, "\n"
print "Monster\n", testMonster, "\n"
print "Bob attacks Manster with Sword!"
testWeapon = Weapon("Sword",1,0,90,2,10,2,4,"str")
testCharacter.addWeapon(testWeapon)
print(testWeapon)
testWeapon.attack(testCharacter, testMonster)
print(testMonster)

#test file to test stuff

from scripts.creatures.creature import *
from scripts.creatures.character import *
from scripts.items.item import *
from scripts.items.weapon import *
from scripts.rooms.room import *
from scripts.world.world import *
from scripts.user_interface.ui import *

world = World()
ui = UserInterface(world)
world.ui = ui

room1 = Room(1, world=world)
room2 = Room(2, world=world)
room1.connectingRooms = [room1]
room2.connectingRooms = [room2]

player = Character("TEST PLAYER",5,4,4,4,[],[],None,1,0)
monster = Creature("TEST MANSTER",3,3,3,3,[],[],None)
player.moveTo(room1)
monster.moveTo(room2)

weapon = Weapon("TEST WEAPON", 0, 0, 90, 2, 5, 2, 3, "str", world)
player.addWeapon(weapon)
player.moveTo(room2)
weapon.attack(player, monster)

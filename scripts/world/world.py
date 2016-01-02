#world class

class World(object):
    def __init__(self, rooms, creatures, character, ui):
        self.rooms = rooms #dict of rooms
        self.creatures = creatures
        self.character = character
        self.ui = ui
    def display(self, txt):
        self.ui.display(txt)
    def prompt(self):
        return self.ui.prompt(txt)
    def attack(self, attacker, defender, weapon, damage):
        if damage:
            self.display(str(attacker)+" attacks "+str(defender)+" with his "+str(weapon)+" for "+str(damage)+" damage!")
        else:
            self.display(str(attacker)+" attacks "+str(defender)+" with his "+str(weapon)+" and MISSES")
    def changeRoom(self, creature, roomTo):
        self.display(str(creature)+" enters "+str(roomTo))

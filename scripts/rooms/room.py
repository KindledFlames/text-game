#room class

class Room(object):
    def __init__(self, creatures, number, hasPlayer=False, connectingRooms, world):
        self.creatures = creatures
        for creature in creatures:
            creature.room = self
        self.number = number
        self.hasPlayer = False
        self.connectingRooms = connectingRooms
        self.world = world
    def addCreature(self, creature):
        self.creatures.append(creature)
    def playerEnters(self):
        self.hasPlayer = True
    def playerExits(self):
        self.hasPlayer = False
    def __str__(self):
        return "Room "+str(self.number)

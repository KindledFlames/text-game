#room class

#rooms are the building blocks of this game
#the player character can only interact with the creatures,
#objects, items, etc that are in the same room they are in

class Room(object):
    def __init__(self, creatures, number, hasPlayer=False, connectingRooms, world):
        #Question: should rooms have names?
        self.creatures = creatures #list of creatures in the room
        for creature in creatures: #set all creatures' room's to this room
            creature.room = self
        self.number = number
        self.hasPlayer = False #to-do change this to hasPlayer
        self.connectingRooms = connectingRooms
        self.world = world
    def addCreature(self, creature): #add creature to room
        if None!=creature.room:
            creature.room.removeCreature(creature) #remove creature from it's old room
        self.creatures.append(creature)
        creature.room = self
        world.changeRoom(creature, self)
    def removeCreature(self, creature):
        try:
            self.creatures.remove(creature)
            return True #return true if the creature was in the room and has now been removed
        except ValueError:
            return False #return false if the creature wasn't in the room
    def playerEnters(self):
        self.hasPlayer = True
    def playerExits(self):
        self.hasPlayer = False
    def __str__(self): #override str method. returns "Room " and then the number
        return "Room "+str(self.number)

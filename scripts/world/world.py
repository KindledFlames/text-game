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

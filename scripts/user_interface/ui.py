#user interface class

class UserInterface(object):
    def __init__(self, world):
        self.world = world
    def display(self, txt):
        print txt
    def prompt(self):
        return raw_input()

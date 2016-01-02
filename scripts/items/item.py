#item class

class Item(object):
	def __init__(self, name, weight, number): #simple constructor
		self.name = name
		self.weight = weight
		self.number = number
	def __str__(self): #overrides str method. outputs the item's string name
		return self.name
	def fullName(self): #outputs the item's full name, defined as the item's name and number
		return self.name + (str(self.number) if self.number!=0 else "")

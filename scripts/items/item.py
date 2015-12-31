#item class

class Item(object):
	def __init__(self, name, weight, number):
		self.name = name
		self.weight = weight
		self.number = number
	def __str__(self):
		return self.name
	def fullName(self):
		return self.name + (str(self.number) if self.number!=0 else "")
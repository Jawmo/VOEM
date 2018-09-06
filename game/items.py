from language import *

class Item():
	def __init__(self, name, item_type, description,
				 attributes, value, weight):
		self.name = name
		self.item_type = item_type
		self.description = description
		self.attributes = attributes
		self.value = value
		self.weight = weight

class Weapon(Item):

	def __init__(self, weapon_range, weapon_type, ammo_type, damage):
		self.weapon_range = weapon_range
		self.weapon_type = weapon_type
		self.ammo_type = ammo_type
		self.damage = damage
		
		super.__init__(item_type="weapon")

class Sidearm(Weapon):

	def __init__(self, ammo_type):
		self. ammo_type = ammo_type

		super.__init__(weapon_range = "far",
					   weapon_type="sidearm",
					   ammo_type="9mm",
					   damage=50)

class Pistol9mm(Weapon):

	def __init__(self):
		super.__init__(ammo_type = "9mm")

items = {
	1: {"name"  		:	"pistol", 
		"class"			:	Sidearm,
		"description" 	:	"It's a gun.",
		"attributes" 	:	[],
		"value"			:	5000,
		"weight"		:	5}
}
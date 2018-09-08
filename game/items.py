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
		self.damage = damage
		super.__init__(item_type="weapon")

	def load_weapon(self, command_input, second_input):
		pass

class Sidearm(Weapon):
	def __init__(self, ammo_type, loaded):
		self. ammo_type = ammo_type
		self.loaded = False
		super.__init__(weapon_range = "far",
					   weapon_type="sidearm",
					   damage=50)

class Pistol9mm(Weapon):
	def __init__(self):
		super.__init__(ammo_type = "9mm")

### Weapon Ammunition

class Ammo(Item):
	def __init__(self, description, ammo_type, current_ammo, max_ammo):
		self.description = description
		self.ammo_type = ammo_type
		self.current_ammo = 10
		self.max_ammo = 10

class Ammo9mm(Ammo):
	def __init__(self):
		super.__init__(description="It's a standard 9mm magazine.", ammo_type="9mm")


items = {
	1: {"name"  		:	"pistol", 
		"class"			:	Sidearm,
		"ammo"			:	False,
		"description" 	:	"Solid sidearm. Looks like it'll take a 9mm magazine.",
		"attributes" 	:	[],
		"value"			:	5000,
		"weight"		:	5},
	2: {"name"  		:	"magazine", 
		"class"			:	Ammo9mm,
		"description" 	:	"It looks like a 9mm magazine.",
		"attributes" 	:	[],
		"value"			:	5000,
		"weight"		:	5,
		"ammo_type"		:	"9mm",
		"current_ammo"	: 	10,
		"max_ammo"		:	10,}
}
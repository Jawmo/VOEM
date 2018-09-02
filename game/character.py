import items

class Character():
	def __init__(self, char_type, name, hp, inventory, in_room, temper):
		self.char_type = char_type
		self.name = name
		self.hp = hp
		self.inventory = inventory
		self.in_room = in_room
		self.temper = temper

	def is_alive(self):
		return self.hp > 0

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)

	def view_inventory(self):
		for item in self.inventory:
			print("You have " + str(item.amt) + " " + str(item.name) + ".")

	def look_room(self):
		print("{}".format(self.in_room["name"]))
		print("{}.".format(self.in_room["desc"]))
		print("Exits: {}".format(", ".join(self.in_room["exits"])))

	def navigate(self, hotkey):
		if self.direction == "north":
			hero.in_room = 
		elif self.direction == "east":
		elif self.direction == "south":
		elif self.direction == "west":
		else:
			print("You don't see a way {}.")

	def flee(self):
		pas

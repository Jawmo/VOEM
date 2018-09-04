import items
from rooms import *

class Character():
	def __init__(self, name, hp, level, inventory, in_room):
		self.name = name
		self.hp = hp
		self.level = level
		self.inventory = inventory
		self.in_room = in_room

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
		print("{} You also see {}".format(self.in_room["desc"], ", ".join(Room.items_in_room(self.in_room["items"]))))
		print("Exits: {}".format(", ".join(self.in_room["exits"])))

	def nav_north(self):
		direction = "north"
		if direction in self.in_room["exits"]:
			self.in_room = rooms[self.in_room["exits"][direction]]
			Character.look_room(self)
		else:
			print (f"You can't go {direction}.")

	def nav_east(self):
		direction = "east"
		if direction in self.in_room["exits"]:
			self.in_room = rooms[self.in_room["exits"][direction]]
			Character.look_room(self)
		else:
			print (f"You can't go {direction}.")

	def nav_south(self):
		direction = "south"
		if direction in self.in_room["exits"]:
			self.in_room = rooms[self.in_room["exits"][direction]]
			Character.look_room(self)
		else:
			print (f"You can't go {direction}.")

	def nav_west(self):
		direction = "west"
		if direction in self.in_room["exits"]:
			self.in_room = rooms[self.in_room["exits"][direction]]
			Character.look_room(self)
		else:
			print (f"You can't go {direction}.")

class Player(Character):

	def __init__(self, name, inventory, in_room):
		super().__init__(name, 100, 1, inventory, in_room)

class NPC(Character):
	pass
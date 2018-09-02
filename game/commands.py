import items
from character import *

def available_commands(self):
	moves = []
	moves.append(ViewInventory())
	moves.append(LookRoom())
	moves.append(NavigateNorth())
	return moves

class Command():
	def __init__(self, method, hotkey, name, **kwargs):
		self. method = method
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs

	def __str(self):
		return "{}: {}".format(self.hotkey, self.name)

class ViewInventory(Command):
	def __init__(self):
		super().__init__(method=Character.view_inventory,
						 name="View Inventory",
						 hotkey="i")

class LookRoom(Command):
	def __init__(self):
		super().__init__(method=Character.look_room,
						 name="Look",
						 hotkey="l")

class NavigateNorth(Command):
	def __init__(self):
		self.direction = "north"
		super().__init__(method=Character.navigate,
						 name="Move north.",
						 hotkey=["n", "north"])

# class NavigateEast(Command):
# 	def __init__(self):
# 		self.direction = "e"
# 		super().__init__(method=Character.nav_east, name="Move east.", hotkey="e", "east")

# class NavigateSouth(Command):
# 	def __init__(self):
# 		self.direction = "s"
# 		super().__init__(method=Character.nav_south, name="Move south.", hotkey="s", "south")

# class NavigateWest(Command):
# 	def __init__(self):
# 		self.direction = "w"
# 		super().__init__(method=Character.nav_west, name="Move west.", hotkey="w", "west")

# verbs_action = {
# 	1: {"name"  :  "look",
# 	    "func"  :  "look",
# 	    "desc"  :  "Displays your location information."},
# 	2: {"name"  :  "get",
# 	    "func"  :  "get_item",
# 	    "desc"  :  "Picks up an item."},
# }

		# for i in verbs_action:
		# 	if command in verbs_action[i]['name']:
		# 		return verbs_action[i]['func']
		
		# print(verbs_action[i]['func'])

# def get_item(self, item):
# 	name = "get"
# 	func = Inventory.add_to_inventory(item)
# 	desc = "Picks up an item."
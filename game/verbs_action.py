verbs_action = {
	1: {"name"  :  "look",
	    "func"  :  "look",
	    "desc"  :  "Displays your location information."},
	2: {"name"  :  "get",
	    "func"  :  "get_item",
	    "desc"  :  "Picks up an item."},
}

class Verb():
	def __init__(self, command, func, desc, item=""):
		self.command = command
		self.func = func
		self.desc = desc
		self.item = item

	def perform(self):
		print(self)



		# for i in verbs_action:
		# 	if command in verbs_action[i]['name']:
		# 		return verbs_action[i]['func']
		
		# print(verbs_action[i]['func'])

# def get_item(self, item):
# 	name = "get"
# 	func = Inventory.add_to_inventory(item)
# 	desc = "Picks up an item."
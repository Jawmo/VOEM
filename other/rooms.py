from items import *

class Room():
	def __init__(self, room_id, title="Blank Title", description="Blank Desc", items=[], env_type="Blank Env", in_out="In or Outside", exits=[]):
		self.room_id = uuid.uuid1()
		self.title = title
		self.description = description
		self.items = items
		self.env_type = env_type
		self.in_out = in_out
		self.exits = exits

	def __repr__(self):
		return("{}\n{}\nExits: {}\n").format(self.title, self.description, self.exits)

	def items_in_room(self):
		
		contents = self
		converted_contents = []
		for i in contents:
			if len(contents) == 1:
				i = Item.a_an(i)
			elif i in contents[-1]:
				i = "and " + Item.a_an(i)
			else:
				i = Item.a_an(i)
			converted_contents.append(i)

		return converted_contents

compass = ["n", "e", "s", "w", "north", "east", "south", "west"]

rooms = {
	1: {"name"  :  "Escape Pod", 
		"desc"  :  "The egg-shaped pod houses just enough room for you to stand up and stretch your legs. A computer panel intermittently beeps nearby.", 
		"exits" :  {"north": 2, "east": 3},
		"items" :  [Pistol().name, Pistol().name]},
	2: {"name"  :  "Second Room", 
	    "desc"  :  "This is the second room.", 
	    "exits" :  {"south": 1, "east": 4},
	    "items" :  ["test"]},
	3: {"name"  :  "Third Room", 
	    "desc"  :  "This is the third room.", 
	    "exits" :  {"west": 1},
	    "items" :  ["something", "bird", "test"]},
	4: {"name"  :  "Fourth Room", 
	    "desc"  :  "This is the fourth room.", 
	    "exits" :  {"west": 2},
	    "items" :  ["test"]},
}
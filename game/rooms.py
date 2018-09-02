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

compass = ["n", "e", "s", "w", "north", "east", "south", "west"]

rooms = {
	1: {"name"  :  "The Void", 
		"desc"  :  "This is the first room. You see nothing. No floor, no walls, just blackness.", 
		"exits" :  {"north": 2, "east": 3},
		"items" :  ["9mm pistol", "apple"]},
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
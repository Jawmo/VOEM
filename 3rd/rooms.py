from items import *
from language import *

class Room():
	def __init__(self, name, description, exits, room_inventory):
		self.name
		self.description
		self.exits
		self.room_inventory

	def room_description(self):
		print(self.current_room["name"])
		print("{} You also see {}.".format(self.current_room["desc"], ", ".join(converted_contents(self.current_room["items"]))))
		print("Exits: {}".format(", ".join(self.current_room["exits"])))


compass = ["n", "e", "s", "w", "north", "east", "south", "west"]

rooms = {
	1: {"name"  :  "Escape Pod", 
		"desc"  :  "The egg-shaped pod houses just enough room for you to stand up and stretch your legs. A computer panel intermittently beeps nearby.", 
		"exits" :  {"north": 2, "east": 3},
		"items" :  ["item", "dead fish"]},
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
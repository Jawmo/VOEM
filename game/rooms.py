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
		print("{}".format(self.current_room["desc"]), end=" ")
		if any(self.current_room["items"]):
			print("You also see {}.".format(", ".join(converted_contents(self.current_room["items"]))))
		else:
			print("")
		print("Exits: {}".format(", ".join(self.current_room["exits"])))

		# print(Ammo.description)
		# print(Ammo9mm)
class Ship(Room):
	def __init__(self, size, engine, sensors, storage, doors):
		self.size = size
		self.engine = engine
		self.sensors = sensors
		self.storage = storage
		self.doors = doors

class Cutlass(Ship):
	def __init__(self):
		pass
	super.__init__(name="cutlass",
				   description="A simple console stands before the pilot seat.",
				   exits="out")

compass = ["n", "e", "s", "w", "north", "east", "south", "west"]

rooms = {
	1: {"name"  :  "Escape Pod", 
		"desc"  :  "The egg-shaped pod houses just enough room for you to stand up and stretch your legs. A computer panel intermittently beeps nearby.", 
		"exits" :  {"north": 2, "east": 3},
		"items" :  [items[1]["name"], items[2]["name"], items[2]["name"]]},
	2: {"name"  :  "Second Room", 
	    "desc"  :  "This is the second room.", 
	    "exits" :  {"south": 1, "east": 4},
	    "items" :  []},
	3: {"name"  :  "Third Room", 
	    "desc"  :  "This is the third room.", 
	    "exits" :  {"west": 1},
	    "items" :  []},
	4: {"name"  :  "Fourth Room", 
	    "desc"  :  "This is the fourth room.", 
	    "exits" :  {"west": 2},
	    "items" :  []},
}

ships = {
	1: {"ship_class"	:	"Cutlass",
		"name"  		:	"Cutlass | Bridge", 
		"desc"  		:	"You see the captain's chair and a console.", 
		"exits" 		:	{"out": []},
		"items" 		:	[items[1], apple]},
}
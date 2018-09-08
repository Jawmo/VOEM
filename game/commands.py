from rooms import *
from character import *
from items import *

def do_this(self):
	print("It works!")

def show_all_commands(self):
	for i in all_commands:
		print("Command:", all_commands[i]["hotkey"])
		print("  ", all_commands[i]["description"])

def object_description(self, command_input, second_input):
	if second_input == "":
		Room.room_description(self)
	else:

		if second_input in self.current_room["items"]:
			for i in items:
				if second_input in items[i]["name"]:
					print("You look at the {} on the floor. {}".format(items[i]["name"],
																	   items[i]["description"]))
					break

		else:
			for i in self.inventory:
				if second_input in self.inventory[i]["contents"]:
					print("You look at {} {} {}.".format(", ".join(converted_contents(self.inventory[i]["contents"])),
																		 			  self.inventory[i]["display"],
																		 			  self.inventory[i]["name"]), end=" ")
					for j in items:
						if [items[j]["name"]] == self.inventory[i]["contents"]:
							print(items[j]["description"])

all_commands = {
	1: 	{"command_name"		: 	"look",
		 "need_com_name"	:  	"no",
		 "need_com_input"	:  	"yes",
	 	 "description"		: 	"Display room or object information. 'L' or 'L object'.",
	 	 "hotkey"			: 	"l",
	 	 "function"			: 	object_description},
	2: 	{"command_name"		: 	"view inventory",
		 "need_com_name"	:  	"no",
		 "need_com_input"	:  	"no",
	 	 "description"		:	"View your inventory.",
	 	 "hotkey"			: 	"i",
	 	 "function"			: 	Character.display_inventory},
	3: 	{"command_name"		: 	"north",
	 	 "need_com_name"	:  	"yes",
	 	 "need_com_input"	:  	"no",
	 	 "description"		: 	"Travel north.",
	 	 "hotkey"			: 	"n",
	 	 "function"			: 	Character.navigate},
	4: 	{"command_name"		: 	"east",
	 	 "need_com_name"	:  	"yes",
	 	 "need_com_input"	:  	"no",
	 	 "description"		: 	"Travel east.",
	 	 "hotkey"			: 	"e",
	 	 "function"			: 	Character.navigate},
	5: 	{"command_name"		: 	"south",
	 	 "need_com_name"	:  	"yes",
	 	 "need_com_input"	:  	"no",
	 	 "description"		: 	"Travel south.",
	 	 "hotkey"			: 	"s",
	 	 "function"			: 	Character.navigate},
	6: 	{"command_name"		: 	"west",
	 	 "need_com_name"	:  	"yes",
	 	 "need_com_input"	:  	"no",
	 	 "description"		: 	"Travel west.",
	 	 "hotkey"			: 	"w",
	 	 "function"			: 	Character.navigate},
	7: 	{"command_name"		: 	"get",
	 	 "need_com_name"	:  	"no",
	 	 "need_com_input"	:  	"yes",
	 	 "description"		: 	"Get an object.",
	 	 "hotkey"			: 	"get",
	 	 "function"			: 	Character.add_to_inventory},
	8: 	{"command_name"		: 	"drop",
	 	 "need_com_name"	:  	"no",
	 	 "need_com_input"	:  	"yes",
	 	 "description"		: 	"Drop an object.",
	 	 "hotkey"			: 	"drop",
	 	 "function"			: 	Character.remove_from_inventory},
	9: 	{"command_name"		: 	"help",
	 	 "need_com_name"	:  	"no",
	 	 "need_com_input"	:  	"no",
	 	 "description"		: 	"Display the the commands.",
	 	 "hotkey"			: 	["h", "help"],
	 	 "function"			: 	show_all_commands},
	10:	{"command_name"		: 	"load",
	 	 "need_com_name"	:  	"no",
	 	 "need_com_input"	:  	"yes",
	 	 "description"		: 	"Insert the appropriate ammo or object for this item.",
	 	 "hotkey"			: 	"load",
	 	 "function"			: 	Weapon.load_weapon},
}
from rooms import *
from character import *

def do_this(self):
	print("It works!")

def show_all_commands(self):
	for i in all_commands:
		print("Command:", all_commands[i]["hotkey"])
		print("  Description:", all_commands[i]["description"])
		

all_commands = {
	1: 	{"command_name"		: 	"look",
		 "need_com_name"	:  	"no",
		 "need_com_input"	:  	"no",
	 	 "description"		: 	"Display the room information.",
	 	 "hotkey"			: 	"l",
	 	 "function"			: 	Room.room_description},
	2: 	{"command_name"		: 	"view inventory",
		 "need_com_name"	:  	"no",
		 "need_com_input"	:  	"no",
	 	 "description"		:	"view your inventory.",
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
}
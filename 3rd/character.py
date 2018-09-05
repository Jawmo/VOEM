from language import *
from rooms import *

class Character():
	def __init__(self, character_type, name, genes,
				 hp, level, inventory, current_room):
		self.character_type = character_type
		self.name = name
		self.genes = genes
		self.hp = hp
		self.level = level
		self.inventory = inventory
		self.current_room = current_room

	def is_alive(self):
		return self.hp > 0
	
	def inventory(self):
		inventory = {
			{"head"			:	"",
			 "left_eye"		:	"",
			 "right_eye"	:	"",
			 "left_ear"		:	"",
			 "right_ear"	:	"",
			 "neck"			:	"",
			 "left_arm"		:	"",
			 "right_arm"	:	"",
			 "chest"		:	"",
			 "belt"			:	"",
			 "left_thigh"	:	"",
			 "right_thigh"	:	"",
			 "left_shin"	:	"",
			 "right_shin"	:	"",
			 "left_foot"	:	"",
			 "right_foot"	:	"",
			 }
		}
	
	def remove_from_inventory(self, command_input, second_input):

		if second_input in self.inventory:
			self.inventory.remove(second_input)
			self.current_room["items"].append(second_input)
			print("You drop {}.".format(a_an(second_input)))
		else:
			print("You don't have {}.".format(a_an(second_input)))

	def add_to_inventory(self, command_input, second_input):

		if second_input in self.current_room["items"]:
			self.current_room["items"].remove(second_input)
			self.inventory.append(second_input)
			print("You pick up {}.".format(a_an(second_input)))
		else:
			print("You don't see {}.".format(a_an(second_input)))

	def display_inventory(self):

		if self.inventory == []:
			print(f"You don't have anything, {self.name}.")
		else:	
			print("You have {}.".format(", ".join(converted_contents(self.inventory))))

	def navigate(self, command_name):
		print(command_name)
		if command_name in self.current_room["exits"]:
			self.current_room = rooms[self.current_room["exits"][command_name]]
			Room.room_description(self)
		else:
			print (f"You can't go {command_name}.")
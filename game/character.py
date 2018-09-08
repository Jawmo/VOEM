from language import *
from rooms import *

class Character():
	def __init__(self, character_type, name, genes,
				 hp, xp, inventory, current_room):
		self.character_type = character_type
		self.name = name
		self.genes = genes
		self.hp = hp
		self.xp = xp
		self.inventory = {
			1: {"name"			:	"head",
			 	"display"		:	"on your head",
			 	"contents"		:	[]},
			2: {"name"			:	"left ear",
				"display"		:	"on your",
			 	"contents"		:	[]},
			3: {"name"			:	"right ear",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			4: {"name"			:	"left eye",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			5: {"name"			:	"right eye",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			6: {"name"			:	"neck",
			 	"display"		:	"around your",
			 	"contents"		:	[]},
			7: {"name"			:	"chest",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			8: {"name"			:	"back",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			9: {"name"			:	"left hand",
				"display"		:	"in your",
			 	"contents"		:	[]},
			10: {"name"			:	"right hand",
			 	"display"		:	"in your",
			 	"contents"		:	[]},
			11: {"name"			:	"belt",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			12: {"name"			:	"left_leg",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			13: {"name"			:	"right_leg",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
			14: {"name"			:	"feet",
			 	"display"		:	"on your",
			 	"contents"		:	[]},
		}

		self.current_room = current_room

	def is_alive(self):
		return self.hp > 0
	
	def remove_from_inventory(self, command_input, second_input):

		if second_input in self.inventory[10]["contents"]:
			self.inventory[10]["contents"].remove(second_input)
			self.current_room["items"].append(second_input)
			print("You drop {}.".format(a_an(second_input)))
		elif second_input in self.inventory[9]["contents"]:
			self.inventory[9]["contents"].remove(second_input)
			self.current_room["items"].append(second_input)
			print("You drop {}.".format(a_an(second_input)))
		else:
			print("You don't have {}.".format(a_an(second_input)))

	def add_to_inventory(self, command_input, second_input):

		if second_input in self.current_room["items"]:
			if self.inventory[10]["contents"] == []:
				self.current_room["items"].remove(second_input)
				self.inventory[10]["contents"].append(second_input)
				print("You pick up {}.".format(a_an(second_input)))
			elif self.inventory[9]["contents"] == []:
				self.current_room["items"].remove(second_input)
				self.inventory[9]["contents"].append(second_input)
				print("You pick up {}.".format(a_an(second_input)))
			else:	
				print("You don't have a free hand.")
		else:
			print("You don't see {}.".format(a_an(second_input)))

	def display_inventory(self):

		for item in self.inventory:
			if self.inventory[item]["contents"] == []:
				pass
			else:
				print("You have", end="")
				print(" {} {} {}".format(", ".join(converted_contents(self.inventory[item]["contents"])),
																	 self.inventory[item]["display"], 
																	 self.inventory[item]["name"]), end="")
				print(".", end=" ")

		# final_inv = []
		# for i in self.inventory:
		# 	if self.inventory[i]["contents"] == []:
		# 		pass
		# 	else:
		# 		final_inv.append(self.inventory[i]["contents"])

		# print(final_inv)
		# print("{}".format(", ".join(final_inv)))

		# final_inv = {}
		# for item in self.inventory:
		# 	for sub_item in self.inventory[item]["contents"]:
		# 		if sub_item == []:
		# 			pass
		# 		else:	
		# 			final_inv['name'] = sub_item
		
		# if final_inv == {}:
		# 	print(f"You don't have anything, {self.name}.")
		# else:
		# 	print(final_inv)
		# 	print("You have {}.".format(", ".join(converted_contents(final_inv))))

	def navigate(self, command_name):
		print(command_name)
		if command_name in self.current_room["exits"]:
			self.current_room = rooms[self.current_room["exits"][command_name]]
			Room.room_description(self)
		else:
			print (f"You can't go {command_name}.")
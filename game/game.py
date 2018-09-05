from character import *
from commands import *
from rooms import *
from items import *

### begin game
prompt = "> "

def play():

	print("\nWelcome to the game. Be ready.")
	print("\nWhat is your name, hero?")
	hero = input(prompt).lower()
	hero = Character("human", hero, [], 100, 1, [items[1]["name"]], rooms[1])
	Room.room_description(hero)
	print("")
	print("Type 'help' to see the current command list.")

	end = False
	while not end:

		print("")
		command_input = input(prompt).lower()
		if len(command_input.split()) > 1:
			second_input = command_input.split()[1]
			command_input = command_input.split()[0]

		for i in all_commands:
			if command_input in all_commands[i]["hotkey"]:
				if all_commands[i]["need_com_name"] == "yes":
					all_commands[i]["function"](hero, all_commands[i]["command_name"])
				elif all_commands[i]["need_com_input"] == "yes":
					all_commands[i]["function"](hero, command_input, second_input)
				else:
					all_commands[i]["function"](hero)
				break
		
		# print(f"\nUnknown command: \"{command_input}\" ")


if __name__ == "__main__":
	play()
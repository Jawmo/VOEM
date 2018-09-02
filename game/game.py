from items import *
from character import *
from commands import *
from rooms import *
 
prompt = "> "
 
def play():
	print("\nWelcome to the game. Be ready.")
	print("\nWhat is your name, hero?")
	hero = input(prompt).lower()
	hero = Character("human", hero, 100, [Credits(500)], rooms[1], "normal")

	print("Welcome, {}.\n".format(hero.name))
	Character.look_room(hero)

	all_commands = available_commands(hero)
	for action in all_commands:
		print("Current Moves: \n")
		print(action.name + ": " + action.hotkey + "\n")

	while hero.is_alive():	
		action_input = input(prompt).lower()
		for action in all_commands:
			if action_input == action.hotkey:
				Character.do_action(hero, action, **action.kwargs)
				break
	        # Check again since the room could have changed the player's state
		print("")

if __name__ == "__main__":
	play()
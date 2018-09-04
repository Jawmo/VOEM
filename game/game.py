from items import *
from character import *
from commands import *
from rooms import *
 
prompt = "> "
 
def play():
	print("\nWelcome to the game. Be ready.")
	print("\nWhat is your name, hero?")
	hero = input(prompt).lower()
	hero = Player(hero, [Credits(200)], rooms[1])

	print("Welcome, {}.\n".format(hero.name))
	Character.look_room(hero)

	all_commands = available_commands(hero)
	print("Current Moves: \n")
	for action in all_commands:
		print(action.name + ": " + action.hotkey)

	while hero.is_alive():	
		action_input = input(prompt).lower()
		for action in all_commands:
			if action_input == action.hotkey:
				Character.do_action(hero, action, **action.kwargs)
				break
		print("")

if __name__ == "__main__":
	play()
from player import Player
 
prompt = "> "
 
def play():
	print("\nWelcome to the game. Be ready.")
	print("\nWhat is your name, hero?")
	hero = input(prompt).lower()
	while hero in ["", " ", "  "]:
		print("\nI didn't quite get that, try again.")
		hero = input(prompt).lower()
	hero = Character()

	if hero.is_alive():
		print("Choose an action:\n")
        available_actions = room.available_actions()
        for action in available_actions:
            print(action)
        action_input = input('Action: ')
        for action in available_actions:
            if action_input == action.hotkey:
                player.do_action(action, **action.kwargs)
                break
	        # Check again since the room could have changed the player's state
	        

	print(f"\nUnknown command: \"{command}\" ")
	print("")

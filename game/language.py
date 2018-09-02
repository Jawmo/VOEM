def convert_items(contents):
		
		converted_contents = []
		for i in contents:
			if len(contents) == 1:
				i = a_an(i)
			elif i in contents[-1]:
				i = "and " + a_an(i)
			else:
				i = a_an(i)
			converted_contents.append(i)

		return converted_contents

def a_an(self):

		if self[0] in ["a", "e", "i", "o", "u", "8"]:
			self = "an " + self
		else:
			self = "a " + self
		
		return self
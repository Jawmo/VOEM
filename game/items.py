# items = {
# 	1: {"name"			: "9mm pistol",
# 		"desc"			: "Looks like a 9mm pistol.",
# 		"mat_type" 		: "steel",
# 		"item_category" : "sidearm",
# 		"durability"	: "strong",
# 		"weight" 		: "5",
# 		"value"		 	: "500"},
# }

class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\nValue: {}\nDescription: {}".format(self.name, self.description, self.value)

    def a_an(self):

        if self[0] in ["a", "e", "i", "o", "u", "8"]:
            self = "an " + self
        else:
            self = "a " + self
        
        return self

class Credits(Item):
	def __init__(self, amt):
		self.amt  = amt
		super().__init__(name="Credits",
						 description="A card with your credits. The only way to pay.",
						 value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)

class Pistol(Weapon):
    def __init__(self):
        super().__init__(name="Pistol",
                         description="It's a gun.",
                         value=10,
                         damage=50)
class VideoGameCharacter:
    def __init__(self, name): # defining init with class instance variables name, health and level
        self.name = name
        self.health = 100
        self.level = 1

    def take_damage(self, amount): # 
       return self.health - amount 
    
    def level_up(self):
        self.level += 1
        self.health = 100

    def is_alive(self):
        return True if self.health > 0 else False
    
# I used __init__ as these were permenant variable / information that needed to be present everytime 
# a new instance of the class was created.

# Take damage is a method that returns the health associated with the instace using it - amount
# of damage taken.

# Level up is  a method that will increase the level of the intanse calling it by 1 and reset that
# instaces health to 100. 

# Is alive is a method that returns true if the instances health is above 0, if not the false meaning
# they're dead.

    def attack(self, other_character, damage_amount):
        other_character.take_damage(damage_amount)
        print(f"{self.name} attacked {other_character.name} for {damage_amount} damage!")
              
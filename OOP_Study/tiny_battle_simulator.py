class VideoGameCharacter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        print(f"{self.name} has joined the battle with {self.health} health points and is level {self.level}")

    def take_damage(self, amount):
        self.health -= amount

    def attack(self, other_character, damage_amount):
        other_character.take_damage(damage_amount)
        print(f"{self.name} attacked {other_character.name} for {damage_amount} damage!")

    def is_alive(self):
        return self.health > 0

# Create characters
hero1 = VideoGameCharacter("Luna")
hero2 = VideoGameCharacter("Blaze")

# Battle time!
hero1.attack(hero2, 20)

# Check health after attack
print(f"{hero2.name}'s health is now {hero2.health}")

while hero1.is_alive() and hero2.is_alive():
    hero1.attack(hero2, 20)
    print(f"{hero2.name}'s health is now {hero2.health}")
    if not hero2.is_alive():
        print(f"{hero1.name} is victorious!")
        break

    hero2.attack(hero1, 10)
    print(f"{hero1.name}'s health is now {hero1.health}")
    if not hero1.is_alive():
        print(f"{hero2.name} is victorious!")
        break
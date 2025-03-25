# Step 1: Define your Character class
class Character:
    def __init__(self, name):
        self.name = name

# Step 2: Here’s the data for 3 characters
characters_data = [
    {"name": "Aria", "health": 100, "mana": 50, "strength": 15},
    {"name": "Brock", "health": 150, "armor": 30, "agility": 10},
    {"name": "Cyra", "health": 80, "mana": 70, "magic_resistance": 20}
]

# Loop through characters_data, create Character instances, and dynamically set attributes
character_objects = []

for data in characters_data:
    # TODO: Create a Character instance using data["name"]
    char = Character(data["name"])
    
    # TODO: Use setattr() to load ALL other key/value pairs into the object
    for key, value in data.items():
        setattr(char, key, value)

    # TODO: Add the character object to character_objects list
    character_objects.append(char)


# Step 4: Print out all attributes of each character using __dict__
for char in character_objects:
    print(f"\nCharacter: {char.name}")
    print("Attributes:")
    # TODO: Loop through char.__dict__ and print attribute names + values
    for key, value in char.__dict__.items():
        print(f"{key}: {value}")

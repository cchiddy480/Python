# This is a simple project ot practise OOP concepts in Python

# Scenario: An italian family-style restaurant has expereienced growth and organization needs to be
# improved via a software solution.

# Making Menus
# Initilization of brunch, early-bird, and kids menus data
brunch = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}

early_bird = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro stagioni': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
}

dinner = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00
}

kids = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}


# Creating Menu class
# Menu class will have name, items, start_time, and end_time as attributes
# Menu class will have a string representation method
# Menu class will store menu items and their prices
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # Method to represent Menu and timings
    def __repr__(self):
        return self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time)
    
    # Menu method to calculate bill
    def calculate_bill(self, purchased_items):
        total = sum([self.items[item] for item in purchased_items])
        return f"Total bill: £{total:.2f}"

brunch = Menu('Brunch', brunch, 11, 16)
early_bird = Menu('Early Bird', early_bird, 15, 18)
dinner = Menu('Dinner', dinner, 17, 23)
kids = Menu('Kids', kids, 11, 21)

# Testing the Menu class
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Creating Franchise class
# Franchise class will have address, menus, and name as attributes
# Franchise class will have a string representation method
# Franchise class will store multiple menus

class Frachise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Method to represent Franchise
    def __repr__(self):
        return self.name + ' franchise located at ' + self.address
    
    # Method to return available menus
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

# Testing the Franchise class    
flagship_store = Frachise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Frachise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))
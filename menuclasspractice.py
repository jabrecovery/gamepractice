from datetime import datetime

class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return self.address

    def available_menu(self, time):
        ava_menu = []
        for menus in self.menus:
            if time > self.start_time and time < self.end_time:
                ava_menu.append(menus)
        return ava_menu

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (f'{self.name} menu is available from {self.start_time} - {self.end_time}')

    def calculate_bill(self, purchased_items):
        total_bill = 0
        for item in purchased_items:
            total_bill += self.items[item]
        print(total_bill)




brunch_items = {
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
early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}

brunch_menu = Menu('Brunch', brunch_items, '1100', '1600')
kids_menu = Menu('Kids', kids_items, '1100', '2100')
early_bird = Menu('Early-Bird Dinner', early_bird_items, '1500', '1800')
dinner_menu = Menu('Dinner', dinner_items, '1700', 2300)

brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])

menus = [brunch_menu,kids_menu, early_bird, dinner_menu]

flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

flagship_store.available_menu('1200')
# Creating a restaurant system
# Making the Menus
class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time = self.end_time)
  
  def calculate_bill(self,*purchased_items):
    return sum(self.items[item] for item in purchased_items)
#     total_price = 0
#     for purchased_item in purchased_items:
#       total_price += self.items[purchased_item]
#     return total_price
        
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu('Brunch', brunch_items, 1100, 1600)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}

early_bird = Menu('Early_bird', early_bird_items, 1500, 1800)

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
} 

dinner = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu('Kids', kids_items, 1100, 2100)

print(brunch)
brunch_bill = brunch.calculate_bill('pancakes','home fries','coffee')
print('Brunch bill:', brunch_bill)

early_bird_bill = early_bird.calculate_bill('salumeria plate','mushroom ravioli (vegan)')
print('Early bird bill:', early_bird_bill)

# Creating the Franchises
class franchise():
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return 'Franchise: {address}'.format(address = self.address)
  
  def availabe_menus(self,time):
    menus = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        menus.append(menu)
    return menus
        
flagship_store = franchise('1232 West End Road',[brunch,early_bird,dinner,kids])    

new_installment = franchise('12 East Mulberry Street',[brunch,early_bird,dinner,kids])

print(new_installment.availabe_menus(1200))

print(new_installment.availabe_menus(1700))

# Creating Businesses
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
aprepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50  
}

aprepas_menu = Menu('Take a\' Arepa', aprepas_menu_items, 1000, 2000 )

aprepas_place = franchise('189 Fitzgerald Avenue',aprepas_menu)

basta = Business('Basta Fazoolin\' with my Heart',[flagship_store,new_installment])

arepa = Business("Take a' Arepa",[flagship_store,new_installment])
print(arepa.franchises[0])

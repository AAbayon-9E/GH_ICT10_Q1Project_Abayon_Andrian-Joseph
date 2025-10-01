from pyscript import display


restuarant_name = '❀⋆Kacha Casa.ೃ'  #  String
owner_name = 'Ryan Abayon'  # String
year_established = 'Since 1987'  # Integer
popular_item_price = '100 pesos'  # Integer
has_delivery = True  # Boolean
product_names = ['Watermelon', 'Coconut', 'Mango', 'Banana']  # List
business_hours = '24 hours'  # String
menu_prices = ['Add-ons = 50pesos', 'Toppings = 100pesos', '12Oz = 150pesos', '16Oz = 200pesos']  # List
common_allergens = ['Nuts', 'Dairy', 'Flour']  # List
tax_rate= '0.09'  # Float


display(restuarant_name, f'Owner: {owner_name}', year_established,target='diva')

display(menu_prices, f'Flavors: {product_names}', f'Allergens: {common_allergens}', target='diva2')
display(business_hours, target='diva3')

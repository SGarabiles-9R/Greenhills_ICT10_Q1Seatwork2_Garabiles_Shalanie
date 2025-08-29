from pyscript import display

restaurant_name = 'Dummy Store' # String
owner_name = 'Dummy' # String
year_establish = 2001 # Integer
popular_item_price = 100 # Integer
has_delivery = True # Boolean
product_names = ['Bread', 'Bloxy Cola', 'Cheezburger', 'Witches Brew', 'Slateskin Potion'] # List
business_hours = '9 am to 11 pm' # String
menu_prices = ['5', '10', '30', '100', '150'] # List
tax_rate = 0.8 # Integer

# Introduction Div
display(f'Hello! I am {owner_name}! Welcome to my {restaurant_name}!', target='intro')
display(f'I made this store back in {year_establish} and trust me, all my prices are loved throughout the years!', target='intro')
display(f'Hey! Check out my {product_names[2]} for only {popular_item_price} TIX!', target='intro')
# Card Divs

    # Card 1
display(f'{product_names[0]} for {menu_prices[0]} TIX', target='desc1')

    # Card 2
display(f'{product_names[1]} for {menu_prices[1]} TIX', target='desc2')

    # Card 3
display(f'{product_names[2]} for {menu_prices[3]} TIX', target='desc3')


# Delivery Div
display(f'Your favorite goods are ready to now ready to deliver right to your doorstep!', target='delivery')
display(f'from {business_hours}!', target='delivery')

display(f'With a small Tax of {tax_rate}% of your order!', target='tax')

# Footer Div
display(f'Garabiles, Shalanie Lanette G. || 10 - RUBY', target='footer')


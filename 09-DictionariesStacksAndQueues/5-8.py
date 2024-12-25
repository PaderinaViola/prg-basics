# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}
total_cart = 0
# Calculate total cost
for key, values in cart.items():
    if key in prices:  # Check if the item is in the price list
        total_cart += prices[key] * values
print(total_cart)
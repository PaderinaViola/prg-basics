price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key, values in price_list.items():
    print(f"{key}: {values}$")

total = 0
for value in price_list.values():
    total += value

print(f"Total before: {total:.2f}$")

for key, values in price_list.items():
    price_list[key] = values * 0.9

for key, values in price_list.items():
    print(f"{key}: {values:.2f}$")

total_new = 0
for value in price_list.values():
    total_new += value

print(f"Total after: {total_new:.2f}$")
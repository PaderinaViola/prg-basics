a = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for key, value in a.items():
    print(f"{key}: {value}")

total = 0
for value in a.values():
    total += value
print(f"the total number of products in the store: {total}")
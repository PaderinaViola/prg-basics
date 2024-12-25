text = "vehicle.txt"

province_mapping = {}
with open(text, 'r') as file:
    content = file.read()
    for row in content:
        province, letter = row
        province_mapping[letter] = province

;lkjhgf
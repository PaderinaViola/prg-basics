arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
arr_sorted = list(map(lambda x: f"{x[0].upper()}, {x[1]}", arr))
for y in arr_sorted:
    print(y)
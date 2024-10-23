number_hours = int(input("Enter the number of hours of parking: "))
if number_hours > 6:
    print(f"Pay 20 zl")
elif number_hours >= 3 and number_hours <= 6:
    print(f"Pay 15 zl")
elif number_hours >= 1 and number_hours <= 2:
    print(f"Pay 5 zl")
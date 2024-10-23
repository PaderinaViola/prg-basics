age = int(input("Enter your age: "))
if age >= 65:
    print(f"You are a senoir")
elif age >=20 and age <= 64:
    print(f"You are an adult")
elif age >= 13 and age <= 19:
    print(f"You are a teen")
elif age < 13:
    print(f"You are just a child")
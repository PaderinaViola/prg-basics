cm = 170
feet = cm/30.48
feet = round(feet, 1)
inches = (cm % 30.48) / 2.54
inches = round(inches, 1)
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
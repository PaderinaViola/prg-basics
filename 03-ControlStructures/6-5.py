###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input ("Tell me the temprature: "))
if temperature > 35:
    print(f"It is extermely hot")
elif temperature > 30:
    print(f"It is hot")
elif temperature >= 15:
    print(f"It is warm")
elif temperature >= 0:
    print(f"It is cold")
else:
    print(f"Warning, you are frosting lol")
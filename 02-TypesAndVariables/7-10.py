import random
computer = random.randint(1,6)
# YOUR TURN
you = int(input("Enter a number from 1 to 6: "))
won = you == computer
print(f'You won: {won}')
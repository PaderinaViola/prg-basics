amount = int(input("Enter the amount in PLN: "))
coin_5 = amount // 5 #we divide our entered number by five and if its not integer, we need to divide everything that is left further
amount = amount % 5  
coin_2 = amount // 2
amount = amount % 2 
coin_1 = amount // 1 
print(f"The amount of PLN {coin_5 * 5 + coin_2 * 2 + coin_1} in coins:")
print(f"5 PLN coins: {coin_5}")
print(f"2 PLN coins: {coin_2}")
print(f"1 PLN coins: {coin_1}")
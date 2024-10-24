#Read a decimal number from the keyboard. 
# Divide the number by 2 and note the remainder.
# Divide the quotient obtained by 2 and note the remainder.
# Repeat the same process till we get 0 as the quotient.
# Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
decimal_number = int(input("Enter a decimal number: "))
binary_number = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number //= 2
print(f"The binary representation is {binary_number}")
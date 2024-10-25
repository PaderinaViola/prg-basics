###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter your letter: ")
print(f"{letter}")

import math
number = '20303'
number_new = int(number)
print(f"number representing the string: {number_new}")

number_dec = 304
number_binary = bin(number_dec)
print(f"Binary number is {number_binary}")

number_hex = hex(number_dec)
print(f"Binary number is {number_hex}")

sign = '€'
sign_new = ord(sign)
print(f"integer representing the Unicode code: {sign_new}")

value = -17
abs_value = abs(value)
print(f"absolute value of -17: {abs_value}")
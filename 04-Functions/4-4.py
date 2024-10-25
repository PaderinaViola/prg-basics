###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0

    if number < 0:
        number = abs(number)
    number_new = str(number)
    for digit in number_new:
        ndigit = int(digit)
        sum += ndigit
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
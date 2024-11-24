def f(number):
    number_str = str(number)
    sum_number = 0
    for digits in number_str: #count() counts how many times the (digit) used in string
        if number_str.count(digits) > 1:
            digits_int = int(digits)
            sum_number += digits_int * number_str.count(digits)
            number_str = number_str.replace(digits, '')
    return sum_number

print(f(1027))
print(f(230335))
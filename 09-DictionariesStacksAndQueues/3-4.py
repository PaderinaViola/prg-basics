def binary_ex(number):
    collection = []
    while number != 0:
        numb_rem = number % 2
        numb_count = number / 2
        collection.append(numb_rem)
        number = int(numb_count)
    if number == 0:
        return collection[::-1]

number = int(input("Enter your number: "))
for i in binary_ex(number):
    print(i, end="")
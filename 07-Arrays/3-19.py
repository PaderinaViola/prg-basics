def check(arr):
    i = float(input("Enter the real value: "))
    counter = 0
    for num in arr:
        if num > i:
            counter += 1
    return counter

array = [34.5, 32.9, 67, 98, 23]

print(check(array))
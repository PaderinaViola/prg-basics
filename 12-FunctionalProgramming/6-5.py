arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
arr_divisible = list(filter(lambda x: x%2 == 0 and x%3 == 0, arr))
print(arr_divisible)
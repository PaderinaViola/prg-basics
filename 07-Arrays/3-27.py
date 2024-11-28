arr = [
       [2, 7, 3, 9],
       [12, 1, 34, 76]
]

def arro(num):
       for row in num:
              for value in row:
                     print(value, end=" ")
              print()

arro(arr)

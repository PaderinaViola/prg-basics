arr= [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7]
]
arr_new = []
print("Before: ")
for rows_what in arr:
    print(" ".join(map(str, rows_what)))

def swapping(arr):
    for _ in range(len(arr)):
        arr[0], arr[2] = arr[2], arr[0]
        return arr

print("After: ") 
for rows_what in swapping(arr):
    print(" ".join(map(str, rows_what)))

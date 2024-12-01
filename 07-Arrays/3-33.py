arr= [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7]
]

print("Before: ")
for rows_what in arr:
    print(" ".join(map(str, rows_what)))
def swap(arr):
    for row in arr:
        row[0], row[-1] = row[-1], row[0] 
    return arr

print("After: ")

for rows_what in swap(arr):
    print(" ".join(map(str, rows_what)))
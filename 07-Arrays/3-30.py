arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for rows in range(len(arr)):
    for columns in range(len(arr)):
        arr[rows][columns] = (rows + 1) * (columns + 1)

for rows_big in arr:
    print(" ".join(map(str, rows_big)))
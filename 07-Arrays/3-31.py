arr = [[-38, 19], 
       [5,40],
       [-7,11],
       [29,16]]

compare_min = [0][0]
compare_max = [0][0]
smallest_num = (0, 0)
biggest_num = (0, 0)
for row in range(len(arr)):
    for column in range(len(arr[row])):
        if arr[row][column] < compare_min:
            compare_min = arr[row][column]
            smallest_num = (row, column)
        if arr[row][column] > compare_max:
            compare_max = arr[row][column]
            biggest_num = (row, column)

print("Smallest num : ", compare_min, smallest_num)
print("Biggest num: ", compare_max, biggest_num)


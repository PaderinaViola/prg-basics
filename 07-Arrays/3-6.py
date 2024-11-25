arr = [15, 8, 31, 47, 2, 19]

total_sum = 0
count = 0

while count < len(arr):
    total_sum += arr[count]  # Add the current element to the total sum
    count += 1  # Move to the next element
total = total_sum / len(arr)
print(total)

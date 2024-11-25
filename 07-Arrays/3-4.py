arr = [-15, 8, -31, 47, -2, 19]

def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop for the number of passes
        for j in range(n - i - 1):  # Inner loop for comparing adjacent elements
            if arr[j] > arr[j + 1]:  # Compare and swap if necessary
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return f"{arr[0]}, {arr[n-1]}"

print(bubble_sort(arr))
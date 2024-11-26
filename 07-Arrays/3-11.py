def bubblesort(array):
    n = len(array)  # Get the length of the array
    for i in range(n):  # Outer loop for the number of passes
        for j in range(n - i - 1):  # Inner loop for comparing adjacent elements
            if array[j] > array[j + 1]:  # Compare and swap if necessary
                array[j], array[j + 1] = array[j + 1], array[j]  # Swap elements
    return array

mass1 = [2, 3, 46, 32, -43, 345, 398, -34]
mass2 = [23, 323, 234, 403, -340, 344, -3434]
mass3 = [96, 9865, 6543, -9876]

print(bubblesort(mass1))
print(bubblesort(mass2))
print(bubblesort(mass3))

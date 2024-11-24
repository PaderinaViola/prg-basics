car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
###
# Bubble sort
#
# Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop for the number of passes
        for j in range(n - i - 1):  # Inner loop for comparing adjacent elements
            if arr[j] > arr[j + 1]:  # Compare and swap if necessary
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return arr  # Return the sorted array

print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(bank_transactions)
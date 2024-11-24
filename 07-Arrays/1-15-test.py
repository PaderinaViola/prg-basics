car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(0, n-2):  # Outer loop for the number of passes  # Inner loop for comparing adjacent elements
        if arr[i] > arr[i + 1]:  # Compare and swap if necessary
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements
    return arr 

print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(bank_transactions)
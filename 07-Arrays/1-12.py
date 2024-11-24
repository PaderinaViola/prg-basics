categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_expenses = max(expenses)
max_index = expenses.index(max_expenses)
max_categories = categories[max_index]
print(max_categories)
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_count = 0
for food in monthly_expenses:
    food_count += food[0]

transport_count = 0
for transport in monthly_expenses:
    transport_count += transport[1]

utilities_count = 0
for utilities in monthly_expenses:
    utilities_count += utilities[2]


week_one = 0
week_two = 0
week_three = 0
week_four = 0
for row_one in monthly_expenses[0]:
    week_one += row_one
for row_two in monthly_expenses[1]:
    week_two += row_two
for row_three in monthly_expenses[2]:
    week_three += row_three
for row_four in monthly_expenses[3]:
    week_four += row_four

total = week_one + week_two + week_three + week_four
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_count)
print('Transport:', transport_count)
print('Utilities:', utilities_count)
print('Week 1:', week_one)
print('Week 2:', week_two)
print('Week 3:', week_three)
print('Week 4:', week_four)
print('---------------')
print('TOTAL:', total)
###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
 # does the employee receive a bonus
bonus = 0.15 # 15%
is_bonus = True

if is_bonus == True:
    total_salary = (basic_salary * bonus) + basic_salary
    print(f"Your total salary with bonus is: {total_salary}")
else :
    print(f"You only receive your basic salary: {basic_salary}")

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
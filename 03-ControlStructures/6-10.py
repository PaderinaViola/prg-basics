years = int(input("Enter the dog's age in human years: "))
count = 0
if years <= 2:
    count += 10.5 * years 
elif years >=3:
    count += 4 * years + 13 
print(f"Your dog in dog age is {count} years old")
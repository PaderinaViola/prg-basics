###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    count = 0
    for line in file:
        count += 1 
        print(f"{count}. {line}", end="")

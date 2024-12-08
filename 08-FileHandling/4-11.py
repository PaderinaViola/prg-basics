text = 'power.txt'
count = 0
with open(text, 'w') as file:
    while count < 100:
        count += 1
        count_second = count ** 2
        count_third = count ** 3
        content = file.write(f"{str(count)},{str(count_second)},{str(count_third)}\n")
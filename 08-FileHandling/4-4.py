my_file = "it_company.csv"
repeat = ''
with open(my_file, 'r') as file:
    content = file.read()
    for lines in content:
        print(lines)
    while repeat == input("Press input:"):
        print(content)

;lkjh
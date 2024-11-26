tuple_var = (50,20,40,50,30,50)
print("Tuple:", ",".join(map(str, tuple_var)))
counter = 0
i = int(input("Value: "))
for i in tuple_var:
    if tuple_var.count(i) > 1:
        counter += 1

print("Number of occurencies: ", counter)

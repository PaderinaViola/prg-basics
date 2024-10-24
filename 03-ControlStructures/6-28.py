n = 20
a = 0
b = 1
for i in range(n):
    a_old = a
    a = b
    b = a_old + b
    print(a)
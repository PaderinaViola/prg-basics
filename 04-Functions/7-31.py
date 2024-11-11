# Tip: xn = x * xn-1
def power(x, n):
    if n == 0:
        return 1
    if x > 1:
        return x * power(x, n-1)

print(power(5, 3))
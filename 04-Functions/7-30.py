def sum_natural(n):
    if n == 1:
        return 1
    if n > 1:
        return n + sum_natural(n-1)
    
print(sum_natural(5))
print(sum_natural(10))
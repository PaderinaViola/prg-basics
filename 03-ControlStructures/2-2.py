###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S':
    print(f'S: Small size')
elif size == 'M':
    print(f"M: Medium size")
elif size == "L":
    print(f"L: Large size")
elif size == "XL":
    print(f"XL: Extra large size")
else:
    print(f"Incorrect symbol")
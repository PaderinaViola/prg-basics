for num in range(1, 31):
    if num % 3 == 0 and num % 5 ==0:
        print(f'BINGO')
    if num % 3 == 0:
        print(f'THREE')
    if num % 5 == 0:
        print(f'FIVE')
    else:
        print(num)
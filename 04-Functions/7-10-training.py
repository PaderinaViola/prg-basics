def f(x,y):
    count = 0
    for numb in range(x,y):
        if numb < 0 and numb % 2 == 0:
            count += 1
        else:
            count += 0
    return count

if __name__ == "__main__":
    print(f(-7, 8))
    print(f(-1, 11))
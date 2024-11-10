def f(x,y):
    count = 0
    for digit in range(x, y+1):
        digit_good = digit % 2
        digit_good_too = digit % 3
        digit_bad = digit % 4
        if digit_good == 0 and digit_good_too == 0 and digit_bad != 0:
            count += digit
    return count

def main():
    print(f(1,20))
    print(f(10,30))

if __name__ == "__main__":
    main()
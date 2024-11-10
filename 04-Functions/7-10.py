def f(x, y):
    count = 0
    for numb in range(x, y):
        x_new = numb % 2
        if numb < 0 and x_new == 0:
            count += 1
        else:
            count += 0
    return count

def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(f(x, y))

if __name__ == "__main__":
    main()
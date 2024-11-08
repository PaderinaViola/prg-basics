def f(amount_to_pay):
    count = 0
    count += amount_to_pay // 5
    amount_to_pay %= 5
    count += amount_to_pay // 2
    amount_to_pay %= 2
    count += amount_to_pay
    return count

def main():
    amount_to_pay = (int(input("Enter: ")))
    print(f(amount_to_pay))

if __name__ == "__main__":
    main()
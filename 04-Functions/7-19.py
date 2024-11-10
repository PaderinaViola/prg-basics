def f(number):
    number_new = str(number)
    sum_repeated = 0
    for digits in number_new:
        if number_new.count(digits) > 1:
            digits_new = int(digits)
            sum_repeated += digits_new * number_new.count(digits)
            number_new = number_new.replace(digits, '')
    return sum_repeated
    
def main():
    print(f(1027))
    print(f(230335))
    print(f(513553007))

if __name__ == "__main__":
    main()
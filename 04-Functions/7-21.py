def f(number1,number2,number3):
    if number1 > number2 and number1 > number3 and number2 > number3:
        max = number1 - number3
        return max
    if number1 > number2 and number1 > number3 and number2 < number3:
        max = number1 - number2
        return max
    if number2 > number1 and number2 > number3 and number1 > number3:
        max = number2 - number3
        return max
    if number2 > number1 and number2 > number3 and number1 < number3:
        max = number2 - number1
        return max
    if number3 > number1 and number3 > number2 and number1 > number2:
        max = number3 - number2
        return max
    if number3 > number1 and number3 > number2 and number1 < number2:
        max = number2 - number1
        return max
    

def main():
    print(f(7,4,9))
    print(f(2,12,8))

if __name__ == "__main__":
    main()
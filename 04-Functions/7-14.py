def f(number1, number2, operator):
    if operator == "+":
        total = number1 + number2
        return total
    if operator == "-":
        total = number1 - number2
        return total
    if operator == "*":
        total = number1 * number2
        return total
    if operator == "%":
        total = number1 % number2
        return total
    if operator == "**":
        total = number1 ** number2
        return total

def main():
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
    operator = input("Operator: ")
    print(f(number1, number2, operator))

if __name__ == "__main__":
    main()
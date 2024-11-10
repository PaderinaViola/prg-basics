def f(number1,number2,number3):
    largest = max(number1,number2,number3)
    smallest = min(number1,number2,number3)
    result = largest - smallest
    return result

def main():
    print(f(7,4,9))
    print(f(2,12,8))

if __name__ == "__main__":
    main()
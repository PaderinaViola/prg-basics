def f(number, even):
    count = 0
    number = str(number)
    for char in number:
        if even == "True":
            if char == "2" or char == "4" or char == "6" or char == "8":
                number = int(number)
                char = int(char)
                count += char
            else:
                count += 0
        elif even == "False":
            if char == "1" or char == "3" or char == "5" or char == "7" or char == "9":
                number = int(number)
                char = int(char)
                count += char
            else:
                count += 0
    return count

def main():
    number = int(input("Enter the number: "))
    even = input("True or False: ")
    print(f(number, even))

if __name__ == "__main__":
    main()
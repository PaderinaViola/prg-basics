def f(binary_number):
    binary_number = str(binary_number)
    for char in binary_number:
        if char == "0" or char == "1":
            return True
        else:
            return False

def main():
    binary_number = (input("Enter "))
    print(f(binary_number))

if __name__ == "__main__":
    main()
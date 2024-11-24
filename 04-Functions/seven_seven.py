def f(binary_number):
    for char in binary_number:
        if char != "1" and char != "0":
            return False
    return True

def main():
    binary_number = (input("Enter "))
    print(f(binary_number))

if __name__ == "__main__":
    main()
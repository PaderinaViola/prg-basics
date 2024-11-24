def f(binary_number):
    for numb in binary_number:
        if numb != "0" and numb != "1":
            return False
    return True

if __name__ == "__main__":
    print(f("101000"))
    print(f("1312e6"))
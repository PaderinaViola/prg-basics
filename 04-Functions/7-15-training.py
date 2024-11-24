def f(detector):
    count = 0
    for sign in detector:
        if sign == "+":
            count += 1
        elif sign == "-":
            count -= 1
        if count >= 3:
            return True
    return False
    
def main():
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))

if __name__ == "__main__":
    main()
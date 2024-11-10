def f(detector):
    count = 0
    max_count = 0
    for action in detector:
        if action == "+":
            count += 1
        elif action == "-":
            count -= 1
            
        max_count = max(max_count, count)
        if max_count >= 3:
            return True
    return False
    
def main():
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))

if __name__ == "__main__":
    main()
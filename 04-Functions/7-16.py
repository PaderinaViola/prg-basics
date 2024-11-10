def f(n):
    a = 0
    b = 1
    for _ in range(n-1):
        a, b = b, a + b
    return a

def main():
    print(f(5))
    print(f(9))

if __name__ == "__main__":
    main()
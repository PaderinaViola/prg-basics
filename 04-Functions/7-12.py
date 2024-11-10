def f(n):
    n_new = (n-1) * "*/" + "*"
    return n_new

def main():
    n = int(input("Enter number: "))
    print(f(n))

if __name__ == "__main__":
    main()
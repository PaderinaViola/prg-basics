def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
        if is_prime == True:
            count += 1
    return num

def main():
    print(f(1))
    print(f(5))

if __name__ == "__main__":
    main()
def f(palindrome):
    palindrome_new = palindrome[::-1]
    if palindrome_new == palindrome:
        return True
    return False

def main():
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))

if __name__ == "__main__":
    main()
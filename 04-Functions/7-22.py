def f(name):
    acronym = "".join([word[0] for word in name.split()])
    return acronym

def main():
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))

if __name__ == "__main__":
    main()
def factorial(n):

    if n==0 or n==1:
        return 1
#this is actually a base case to which function returns after n-1 n finally becoms 1 and 0
    if n > 1:
        return n * factorial(n-1)
    
def main():
    print(factorial(5))

if __name__ == "__main__":
    main()
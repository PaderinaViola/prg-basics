def f(n):
    result = ""
    for char in range(1, n+1):
        char = str(char)
        result += char
    return result

#Якщо просто прописувати як ретьорн чар, то поверне справді тільки перше значення, тому треба використовувати нову змінну
#яка типу як "лічильник", тобто += чaр
#Якщо видає помилки в мейні то скоріш за все не визначила на початку змінну
def main():
    n = int(input("Enter: "))
    print(f(n))

if __name__ == "__main__":
    main()
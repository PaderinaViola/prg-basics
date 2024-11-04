def count(text, letter):
    text = input("Enter your text: ")
    letter = input("Enter your letter: ")
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print(f"The number of letter '{letter}': {count}")
    return count

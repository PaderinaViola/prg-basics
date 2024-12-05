import re
text = input("File name: ")
count_lines = 0

def char(text):
    try:
        count_char = 0
        with open(text, 'r') as file:
            content = file.read()
            for _ in content:
                count_char += 1
        return count_char
    except FileNotFoundError:
        print(f"Error: The file '{text}' does not exist.")



def lines(text):
    try:
        count_lines = 0
        with open(text, 'r') as file:
            content = file.read()
            count_lines = len(content.splitlines())
            return count_lines
    except FileNotFoundError:
        print(f"Error: The file '{text}' does not exist.")

def words(text):
    try:
        count_words = 0
        with open(text, 'r') as file:
            content = file.read()
            count_words = len(content.split())
            return count_words
    except FileNotFoundError:
        print(f"Error: The file '{text}' does not exist.")

print("Number of lines:", lines(text))
print("Number of characters:", char(text))
print("Number of words:", words(text))


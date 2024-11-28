text = "An apple a day keeps the doctor away"
def numb_words(text):
    words = text.split()
    return len(words)

def array(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return words

def alphabet(text):
    words = text.split()
    words.sort()
    return words

print("Text: ", "".join(map(str, text)))
print("Number of words:", numb_words(text))
print("Words from the longest:", ", ".join(map(str, array(text))))
print("Words ordered alphabetically:", ", ".join(map(str, alphabet(text))))
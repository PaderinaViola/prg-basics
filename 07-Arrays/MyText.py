text = "An apple a day keeps the doctor away"
def numb_words(text):
    words = text.split()
    return len(words)

def array(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return words

print(numb_words(text))
print(array(", ".join(text)))
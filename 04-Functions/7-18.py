def f(sentence):
    sentence_new = sentence.replace(" ", "")
    return sentence_new

def main():
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))

if __name__ == "__main__":
    main()
import csv
fantasy = "book_fantasy.txt"
historical = "books_historical.txt"
romance = "books_romance.txt"
classic = "books_classic.txt"

def fantasy_(text):
    with open("books.csv", 'r') as file:
        content_csv = csv.reader(file)
        with open(fantasy, 'w') as file_2:
            next(content_csv)
            for sentence in content_csv:
                        for words in sentence:
                            if words == "Fantasy":
                                file_2.write(f"{", ".join(map(str, sentence))}\n")

fantasy_(fantasy)

def historical_(text):
    with open("books.csv", 'r') as file:
        content_csv = csv.reader(file)
        with open(historical, 'w') as file_2:
            next(content_csv)
            for sentence in content_csv:
                        for words in sentence:
                            if words == "Historical":
                                file_2.write(f"{", ".join(map(str, sentence))}\n")

historical_(historical)

def romance_(text):
    with open("books.csv", 'r') as file:
        content_csv = csv.reader(file)
        with open(romance, 'w') as file_2:
            next(content_csv)
            for sentence in content_csv:
                        for words in sentence:
                            if words == "Romance":
                                file_2.write(f"{", ".join(map(str, sentence))}\n")

romance_(romance)

def classic_(text):
    with open("books.csv", 'r') as file:
        content_csv = csv.reader(file)
        with open(classic, 'w') as file_2:
            next(content_csv)
            for sentence in content_csv:
                        for words in sentence:
                            if words == "Classic":
                                file_2.write(f"{", ".join(map(str, sentence))}\n")

classic_(classic)
file_name = "books.csv"

genre = "Dystopian"

count = 0
with open(file_name) as file:
    for line in file:
        if genre in line:
            count += 1
            print(f"{count}. {line}")


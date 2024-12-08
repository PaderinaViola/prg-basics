import csv
print("GRAPHIC DESIGNERS")
print("=================")
with open('it_company.csv', 'r') as file:
    content_csv = csv.reader(file)
    for row in content_csv:
        for word in row:
            if word == "Graphic Designer":
                print(f"{row[1]} {row[0]},{row[3]}")
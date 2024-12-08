import csv
with open("clothing.csv", 'r') as file:
    content_csv = csv.reader(file)
    next(content_csv)
    for row in content_csv:
        if float(row[5]) < 60 and float(row[6]) < 40:
            print(", ".join(row))
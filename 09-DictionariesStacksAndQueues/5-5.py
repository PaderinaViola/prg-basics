paragraph = "cat dog mouse cat rat cat mouse"
paragraph_new = paragraph.split()
dictionary = {}
for i in paragraph_new:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)

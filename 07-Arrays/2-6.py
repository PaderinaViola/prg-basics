matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for item in range(len(matrix)):
    matrix[item][item] = 1
for row in matrix:
    print(" ".join(map(str, row)))

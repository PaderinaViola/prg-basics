def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def print_m(matrix):
    for rows in matrix:
        print(" ".join(str(i) for i in rows))
sizes = [3, 5, 8]


for size in sizes:
    identity_mat = identity_matrix(size)
    print_m(identity_mat)
    print()
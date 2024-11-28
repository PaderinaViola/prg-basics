def create_2d_arr(x,y):
    return [y*[0]] * x

arr = create_2d_arr(3, 5)
for rows in arr:
    print(" ".join(map(str, rows)))
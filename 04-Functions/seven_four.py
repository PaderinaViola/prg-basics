
def range(h, n, m):
    h = int(input(h))
    n = int(input(n))
    m = int(input(m))
    numb = (n < h < m)
    if numb == True:
        print(f"Yup")
    else:
        print(f"Nope")
    return numb
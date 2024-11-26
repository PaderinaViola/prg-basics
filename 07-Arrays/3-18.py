def second_largest(numb):
    numb_sorted = numb.copy()
    n = len(numb_sorted)
    for i in range(n):  
        for j in range(n - i - 1):  
            if numb_sorted[j] > numb_sorted[j + 1]:  
                numb_sorted[j], numb_sorted[j + 1] = numb_sorted[j + 1], numb_sorted[j]  
    return numb_sorted[-2]

def difference(numb):
    numb_sorted= numb.copy()
    n = len(numb_sorted)
    for i in range(n):  
        for j in range(n - i - 1):  
            if numb_sorted[j] > numb_sorted[j + 1]:  
                numb_sorted[j], numb_sorted[j + 1] = numb_sorted[j + 1], numb_sorted[j]  
    return numb_sorted[-1] - numb_sorted[0]

def median(numb):
    numb_sorted= numb.copy()
    n = len(numb_sorted)
    for i in range(n):  
        for j in range(n - i - 1):  
            if numb_sorted[j] > numb_sorted[j + 1]:  
                numb_sorted[j], numb_sorted[j + 1] = numb_sorted[j + 1], numb_sorted[j] 
    med = n // 2 
    return numb_sorted[med]

def small_big(numb):
    numb_sorted= numb.copy()
    n = len(numb_sorted)
    for i in range(n):  
        for j in range(n - i - 1):  
            if numb_sorted[j] > numb_sorted[j + 1]:  
                numb_sorted[j], numb_sorted[j + 1] = numb_sorted[j + 1], numb_sorted[j] 
    return numb_sorted[0], numb_sorted[-1]
    

arr = [7,3,8,5,2]
print("numb_sorteders:", ",".join(map(str, arr)))
print("Second largest numb_sorteder:", second_largest(arr))
print("Median:", median(arr))
print("Smallest and largest numb_sorteder:", ",".join(map(str, small_big(arr))))
print("numb_sorteders:", "-".join(map(str, arr)))
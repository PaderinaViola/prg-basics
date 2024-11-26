def compare(array1, array2):
    huh_true = False
    if len(array1) == len(array2):
        for i in array1:
            for a in array2:
                if i == a:
                    huh_true = True
    if huh_true == True:
        return f"arrays are the same"
    if huh_true == False:
        return f"arrays are NOT the same"

print(compare(["water","book","sky"], ["water","book","sky"]))
print(compare([True,False], [True,False,True]))
print(compare([5,3,1], [5,3,1]))
print(compare([3,2,1], [3,2]))
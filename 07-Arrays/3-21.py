arr1 = [34, 432, 534, 2, 4329]
arr2 = [34, 534, 2, 4329, 434, 432, 5, 43]
def check(arr1, arr2):
    count = 0
    for a in arr1:
        if a in arr2:
            count += 1
    if count == len(arr1):
      return True
    else:
        return False
print(check(arr1, arr2))
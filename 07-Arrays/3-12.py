arr = [3, 9876, 876, 3, 876, 7776]
counter_unique = []
for i in arr:
    if arr.count(i) == 1:
        counter_unique += [i]

print("Array:", " ".join(map(str, arr)))
print("Unique elements:", " ".join(map(str, counter_unique)))
def occurs(number, array):
        if number in array:
            return True
        else:
            return False

arr = [15, 38, 7, 23, 14]
numb = int(input("Number: "))
print("Array:", " ".join(map(str, arr)))
if occurs(numb, arr) == True:
     print(f"Result: number {numb} appears in the array")
else:
     print(f"Result: number {numb} does NOT appear in the array")
arr = [2,3,7,5,4]
#the array
print(arr)
#number of elements
number_elements = len(arr)
print(number_elements)
first_v = arr[0]
print(first_v)
second_v = arr[1]
print(second_v)
last_v = arr[-1]
print(last_v)
pre_last_v = arr[len(arr)-2]
print(pre_last_v)
sum_f_l = arr[0]  + arr[-1]
print(sum_f_l)
middle = arr[len(arr)//2]
print(middle)
for i in arr:
    print(i, end = " ")
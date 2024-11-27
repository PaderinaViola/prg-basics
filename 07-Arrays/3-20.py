arr = [7,9,2,4,5,6]
even_list = []
odd_list = []
for i in arr:
    if i % 2 == 0:
        even_list.append(i)
    elif i % 2 != 0:
        odd_list.append(i)

even_list.sort()
odd_list.sort()

final = even_list + odd_list
print(final)

#если четное то заносишь в новый лист, сортируешь, создаешь новый лсит для нечетных, сортируешь, складываешь
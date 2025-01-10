names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sorted_names = sorted(names, key=lambda name: len(name))
print("Sorted list by length:")
for n in sorted_names:
    print(n)
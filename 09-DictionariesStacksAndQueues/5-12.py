text = input("Enter your string: ")
import queue
string_queue = queue.LifoQueue()
for letter in text:
    string_queue.put(letter)

while not string_queue.empty():
    char = string_queue.get()
    print(char, end="")

def f(dictionary, x, y):
    total_sum = 0
    for values in dictionary.values():
        total_sum += sum(num for num in values if x <= num <= y)
    return total_sum
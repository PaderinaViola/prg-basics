import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    matches = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.put(char)  # Add opening brackets to the stack
        elif char in ')}]':
            if stack.empty() or stack.get() != matches[char]:
                return False
    if stack.empty():
       return True

if brackets_ok(expression1):
   print("The expression is correct")
else:
   print("The expression is wrong")

if brackets_ok(expression2):
   print("The expression is correct")
else:
   print("The expression is wrong")

if brackets_ok(expression3):
   print("The expression is correct")
else:
   print("The expression is wrong")
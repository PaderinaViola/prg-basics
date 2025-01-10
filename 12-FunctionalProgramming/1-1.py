###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   arith_mean = (x+y)/2
   return arith_mean

# takes two numbers from keyboard
n1 = int(input("give"))
n2 = int(input())

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')
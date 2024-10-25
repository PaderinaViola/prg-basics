import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    formule  = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return formule
result = triangle_area(3,4,5)
result_new = triangle_area(5,12,13)
result_new_new = triangle_area(7,24,25)
print(f'The area of ​​a triangle with sides 3,4,5 is {result}')
print(f'The area of ​​a triangle with sides 5,12,13 is {result_new}')
print(f'The area of ​​a triangle with sides 7,24,25 is {result_new_new}')
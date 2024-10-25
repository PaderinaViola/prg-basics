###
# To use the functions available in an external module,
# you must include that module in your program.
import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

natural_log = math.log1p(5)
print(f"Natural logarithm of 5 is {natural_log}")

angle_in_degrees = 90
angle_in_radians = math.radians(angle_in_degrees)
sinus = math.sin(angle_in_radians)
print(f"The sinus of 90 degrees is {sinus}")
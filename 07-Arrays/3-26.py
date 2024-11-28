import matplotlib.pyplot as plt
import math
x = []
y = []

x = range(0, 361)
y = [math.sin(math.radians(i)) for i in x] 

plt.plot(x, y)
plt.show()

import numpy as np

x = np.arange(2,8,2)
print(x)
x = np.append(x, x.size)
print(x)
x = np.sort(x)
print(x)
print(x[1])


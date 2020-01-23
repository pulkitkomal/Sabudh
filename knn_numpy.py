import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)
rand_array = np.random.randint(low=0, high=12, size=(200, 2))  # Two-dimensional array
# rand_array1 = np.random.randint(low=10, high= 20, size=(200, 2))
# print(rand_array)
# print(rand_array.size)
x = rand_array[:, [0]]  # accessing x column
y = rand_array[:,[1]]  # accessing y column

# x1 = rand_array1[:,[0]]
# y1 = rand_array1[:,[1]]

plt.scatter(x,y, color = 'green')
plt.scatter(x1,y1, color = 'red')
plt.show()






# create a matrix, visualize it, and save it to a file

import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.rand(5, 5)
plt.imshow(matrix, cmap='hot', interpolation='nearest')
# show values of matrix in each cell
plt.colorbar() # show color bar
# show the numbers of 
# for i in range(5):
#     for j in range(5):
#         plt.text(j, i, round(matrix[i, j], 2), ha='center', va='center')

plt.savefig('matrix.png')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# print(matrix)
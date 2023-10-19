import numpy as np

# Create three 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])
join = [[A,B],[C,A]]
D = np.block(join)
# Join the matrices into one 4x4 matrix

print(D)
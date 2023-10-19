import numpy as np

# Create a sample 2D matrix (array)
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Slice a part of the matrix
# Syntax: matrix[start_row:end_row, start_column:end_column]
# The end_row and end_column are not inclusive.

# Example 1: Slicing a submatrix
submatrix = matrix[0:2, 1:3]
print("Submatrix 1:")
print(submatrix)

# Example 2: Slicing rows
rows = matrix[1:3, :]
print("\nSliced Rows:")
print(rows)

# Example 3: Slicing columns
columns = matrix[:, 1:3]
print("\nSliced Columns:")
print(columns)

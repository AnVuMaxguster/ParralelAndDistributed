import numpy as np

# Create a sample matrix
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Define a shift function
def shift_matrix(matrix, direction):
    if direction == "left":
        return np.roll(matrix, shift=-1, axis=1)
    elif direction == "right":
        return np.roll(matrix, shift=1, axis=1)
    elif direction == "up":
        return np.roll(matrix, shift=-1, axis=0)
    elif direction == "down":
        return np.roll(matrix, shift=1, axis=0)
    else:
        raise ValueError("Invalid direction. Choose from 'left', 'right', 'up', or 'down'.")

# Shift the matrix in different directions
shifted_left = shift_matrix(matrix, "left")
shifted_right = shift_matrix(matrix, "right")
shifted_up = shift_matrix(matrix, "up")
shifted_down = shift_matrix(matrix, "down")

# Print the shifted matrices
print("Shifted Left:")
print(shifted_left)

print("\nShifted Right:")
print(shifted_right)

print("\nShifted Up:")
print(shifted_up)

print("\nShifted Down:")
print(shifted_down)

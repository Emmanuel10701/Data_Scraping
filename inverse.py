
import numpy as np

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

# Finding the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

# Display the inverse matrix
print("Original Matrix:")
print(matrix)

print("\nInverse Matrix:")
print(inverse_matrix)

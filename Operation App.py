import numpy as np


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

print("Array 1:", arr1)
print("Array 2:", arr2)


print("\n--- Arithmetic Operations ---")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Square of Array 1:", arr1 ** 2)


print("\n--- Statistical Operations ---")
print("Sum of Array 1:", np.sum(arr1))
print("Mean of Array 1:", np.mean(arr1))
print("Median of Array 1:", np.median(arr1))
print("Standard Deviation of Array 1:", np.std(arr1))
print("Maximum of Array 1:", np.max(arr1))
print("Minimum of Array 1:", np.min(arr1))


print("\n--- Logical Operations ---")
print("Array1 > 3:", arr1 > 3)
print("Array1 == Array2:", arr1 == arr2)


print("\n--- Matrix Operations ---")
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix Addition:\n", matrix1 + matrix2)
print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))
print("Transpose of Matrix 1:\n", matrix1.T)
print("Determinant of Matrix 1:", np.linalg.det(matrix1))
print("Inverse of Matrix 1:\n", np.linalg.inv(matrix1))
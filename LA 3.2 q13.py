import numpy as np


def row_reduce(matrix):
    B = matrix.astype(float)
    n = B.shape[0]

    # Gaussian elimination for upper triangular form
    for i in range(n):
        if B[i, i] == 0:
            for j in range(i + 1, n):
                if B[j, i] != 0:
                    B[[i, j]] = B[[j, i]]  # Swap rows
                    break

        for j in range(i + 1, n):
            if B[j, i] != 0:
                factor = B[j, i] / B[i, i]
                B[j] -= factor * B[i]

    return B


def determinant(matrix):
    if matrix.shape[0] == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    det = 0
    n = matrix.shape[0]
    for col in range(n):
        submatrix = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)
        det += ((-1) ** col) * matrix[0, col] * determinant(submatrix)

    return det


# Define the original matrix
A = np.array([
    [2, 5, 4, 1],
    [4, 7, 6, 2],
    [6, -2, -4, 0],
    [-6, 7, 7, 0]
])

# Perform row reduction
R = row_reduce(A)

# Calculate the determinant using cofactor expansion on the reduced matrix
det = determinant(R)
print("Determinant of the matrix is:", det)

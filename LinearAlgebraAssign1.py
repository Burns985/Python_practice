import numpy as np

# Define the augmented matrix with floating-point numbers
A = np.array([[3.0, -4.0, 2.0, 0.0],
              [-9.0, 12.0, -6.0, 0.0],
              [-6.0, 8.0, -4.0, 0.0]])

# Perform Gaussian elimination
def gaussian_elimination(A):
    n = len(A)
    for i in range(n - 1):
        # Find the pivot element
        pivot = A[i, i]
        if abs(pivot) < 1e-10:
            # Handle cases where the pivot is close to zero (avoid division by zero)
            print("Warning: Pivot element is close to zero. Performing row swapping.")
            for j in range(i + 1, n):
                if abs(A[j, i]) > abs(pivot):
                    A[[i, j]] = A[[j, i]]  # Swap rows
                    pivot = A[i, i]
                    break
        # Check if a valid pivot was found
        if abs(pivot) < 1e-10:
            print("Error: Singular matrix. No solution exists.")
            return None

        # Eliminate elements below the pivot
        for j in range(i + 1, n):
            factor = A[j, i] / pivot
            A[j, :] -= factor * A[i, :]
    return A


# Solve the system using back substitution
def back_substitution(A):
    n = len(A)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # Calculate x_i
        x[i] = (A[i, n - 1] - np.sum(A[i, :i] * x[:i])) / A[i, i]
    return x


# Perform Gaussian elimination
A = gaussian_elimination(A.copy())

# Check if a solution exists
if A is None:
    exit()

# Perform back substitution to find the solution
x = back_substitution(A)

# Print the general solution
print("General solution:")
for i in range(len(x)):
    print(f"x{i + 1} = {x[i]} (free)")

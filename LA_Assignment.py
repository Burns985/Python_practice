# import numpy as np
#
# # Define matrices a1, a2, a3, and b
# a1 = np.array([[1], [-2], [0]])
# a2 = np.array([[0], [1], [2]])
# a3 = np.array([[5], [-6], [8]])
# b = np.array([[2], [-1], [6]])
#
# # Create a matrix containing a1, a2, and a3 as columns
# A = np.concatenate((a1, a2, a3), axis=1)
#
# # Solve the equation Ax = b
# x = np.linalg.lstsq(A, b, rcond=None)[0]
#
# # Check if x exists
# if np.allclose(np.dot(A, x), b):
#     print("b is a linear combination of a1, a2, and a3.")
#     # Round the scalars to 2 decimal places
#     x_rounded = np.round(x.flatten(), 2)
#     print("Scalars (x, y, z):", tuple(x_rounded))
# else:
#     print("b is not a linear combination of a1, a2, and a3.")
print()
# import numpy as np
#
# # Define matrix A and vector b
# A = np.array([[1, 3, -4], [1, 5, 2], [-3, -7, 6]])
# b = np.array([[-2], [4], [12]])
#
# # Construct the augmented matrix
# augmented_matrix = np.concatenate((A, b), axis=1)
#
# # Print the augmented matrix
# print("Augmented Matrix:")
# print(augmented_matrix)
#
# # Solve the system
# solution = np.linalg.solve(A, b)
#
# # Round the solution to whole numbers
# solution_rounded = np.round(solution, decimals=0)
#
# # Print the solution vector
# print("\nRounded Solution Vector:")
# print(solution_rounded)
print()
import numpy as np

# Define the augmented matrix
augmented_matrix = np.array([[9, -1, 0, -1, -4, 50],
                             [-1, 7, -2, 0, -3, -30],
                             [0, -2, 10, -3, -3, 20],
                             [-1, 0, -3, 7, -2, -40],
                             [-4, -3, -3, -2, 12, 0]])

# Extract matrix A and vector b
A = augmented_matrix[:, :-1]  # All rows, all columns except the last
b = augmented_matrix[:, -1]   # All rows, only the last column

# Solve the system
solution = np.linalg.solve(A, b)

# Interpret the solution as loop currents
loop_currents = solution[:-1]  # Exclude the last element which represents a voltage

# Print the solution (loop currents)
print("Loop Currents:")
for i, current in enumerate(loop_currents, start=1):
    print(f"I{i}:", current)



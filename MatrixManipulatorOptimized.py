import numpy as np


def matrix_operation(m1, m2, operation):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Matrices must have the same dimensions.")
        return None

    operations = {
        "add": np.add,
        "subtract": np.subtract,
        "multiply": np.matmul,
    }

    if operation not in operations:
        print("Invalid operation.")
        return None

    return operations[operation](m1, m2)


def transpose(matrix):
    return np.transpose(matrix)


def inverse(matrix):
    if len(matrix) == len(matrix[0]):
        return np.linalg.inv(matrix)
    else:
        print("Inverse can only be found for square matrices.")
        return None


def adjoint(matrix):
    if len(matrix) == len(matrix[0]):
        return np.round(np.linalg.inv(matrix) * np.linalg.det(matrix), 2)
    else:
        print("Adjoint can only be found for square matrices.")
        return None


def prompt_matrix():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            matrix = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    value = float(input(f"Enter value for row {i+1}, column {j+1}: "))
                    row.append(value)
                matrix.append(row)
            return np.array(matrix)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_matrix(matrix):
    print(matrix)


def prompt_matrices(num_matrices):
    matrices = []
    for i in range(num_matrices):
        print(f"Matrix {i+1}:")
        matrix = prompt_matrix()
        matrices.append(matrix)
    return matrices


def continue_program():
    while True:
        try:
            response = input("Do you wish to continue (yes/no)? ").strip().lower()
            if response in ('yes', 'no'):
                return response == 'yes'
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")


def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("Matrix Operations Menu:")
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Find transpose")
        print("5. Find inverse")
        print("6. Find adjoint")
        print("0. Exit")

        choice = get_choice()

        if choice == 1:
            print("Addition")
            num_matrices = int(input("Enter the number of matrices to add: "))
            matrices = prompt_matrices(num_matrices)
            result = np.sum(matrices, axis=0)
            print("Result:")
            print_matrix(result)

        elif choice == 2:
            print("Subtraction")
            num_matrices = int(input("Enter the number of matrices to subtract: "))
            matrices = prompt_matrices(num_matrices)
            result = matrices[0]
            for i in range(1, num_matrices):
                result = matrix_operation(result, matrices[i], "subtract")
            print("Result:")
            print_matrix(result)

        elif choice == 3:
            print("Multiplication")
            num_matrices = int(input("Enter the number of matrices to multiply: "))
            matrices = prompt_matrices(num_matrices)
            result = matrices[0]
            for i in range(1, num_matrices):
                result = matrix_operation(result, matrices[i], "multiply")
            print("Result:")
            print_matrix(result)

        elif choice == 4:
            print("Transpose")
            matrix = prompt_matrix()
            result = transpose(matrix)
            print("Result:")
            print_matrix(result)

        elif choice == 5:
            print("Inverse")
            matrix = prompt_matrix()
            result = inverse(matrix)
            print("Result:")
            print_matrix(result)

        elif choice == 6:
            print("Adjoint")
            matrix = prompt_matrix()
            result = adjoint(matrix)
            print("Result:")
            print_matrix(result)

        elif choice == 0:
            print("Exiting...")
            break

        if not continue_program():
            print("Thank you! Have a lovely rest of the day.")
            break


if __name__ == "__main__":
    main()

import numpy as np


def subtract(m1, m2):
    if not m1 and m2:
        return m1 or m2
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("We do not do that here.")
    else:
        sub_matrix = []
        for i in range(len(m1)):
            new_row = []
            for j in range(len(m1[i])):
                new_row.append(m1[i][j] - m2[i][j])
            sub_matrix.append(new_row)
        return sub_matrix


def add(m1, m2):
    if not m1 and m2:
        return m1 or m2
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("We do not do that here.")
    else:
        sum_matrix = []
        for i in range(len(m1)):
            new_row = []
            for j in range(len(m1[i])):
                new_row.append(m1[i][j] + m2[i][j])
            sum_matrix.append(new_row)
        return sum_matrix


def multiply(m1, m2):
    if not m1:
        return m1
    if len(m1[0]) != len(m2):
        print("We do not do that here.")
    else:
        mul_matrix = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    mul_matrix[i][j] += m1[i][k] * m2[k][j]
        print(mul_matrix)
        return mul_matrix


def transpose(matrix):
    if not matrix:
        return matrix
    transposed = []
    while matrix[0]:
        row = []
        for col in matrix:
            if col:
                row.append(col.pop(0))
            else:
                break
        transposed.append(row)
    return transposed


def m_inverse(matrix):
    if not matrix:
        return matrix
    if len(matrix) != len(matrix[0]) != 2 or len(matrix) != len(matrix[0]) != 3:
        print("Inverse can only be found of 2x2 or 3x3 matrices")
        return
    else:
        if len(matrix) == 2 or len(matrix) == 1:
            inverse = []
            flag = True
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            while matrix[0]:
                flag = not flag
                row = []
                for col in matrix:
                    if col:
                        if flag:
                            row.append(col.pop(0) * -1)
                        else:
                            row.append(col.pop(0))
                    else:
                        break
                    flag = not flag
                inverse.append(row[::-1])
                inverse = inverse[::-1]
            inverse = [[x / det for x in row] for row in inverse]
            print(inverse)
            return inverse

        elif len(matrix) == 3:
            det = np.linalg.det(np.array(matrix))
            vertices = [item for sublist in matrix for item in sublist]
            inverse = [[(vertices[4] * vertices[8]) - (vertices[5] * vertices[7]),
                        ((vertices[1] * vertices[8]) - (vertices[2] * vertices[7])) * -1,
                        (vertices[1] * vertices[5]) - (vertices[2] * vertices[4])],

                       [((vertices[3] * vertices[8]) - (vertices[5] * vertices[6])) * -1,
                        (vertices[0] * vertices[8]) - (vertices[2] * vertices[6]),
                        ((vertices[0] * vertices[5]) - (vertices[2] * vertices[3])) * -1],

                       [(vertices[3] * vertices[7]) - (vertices[4] * vertices[6]),
                        ((vertices[0] * vertices[7]) - (vertices[1] * vertices[6])) * -1,
                        (vertices[0] * vertices[4]) - (vertices[1] * vertices[3])]
                       ]
            inverse = [[round(x / det, 2) for x in row] for row in inverse]
            print(inverse)
            return inverse


def adjoint(matrix):
    if not matrix:
        return matrix
    if len(matrix) != len(matrix[0]):
        print("Adjoint can only be found of 2x2 or 3x3 matrices")
        return
    else:
        if len(matrix) == 2 or len(matrix) == 1:
            adjoin = []
            flag = True
            while matrix[0]:
                flag = not flag
                row = []
                for col in matrix:
                    if col:
                        if flag:
                            row.append(col.pop(0) * -1)
                        else:
                            row.append(col.pop(0))
                    else:
                        break
                    flag = not flag
                adjoin.append(row[::-1])
                adjoin = adjoin[::-1]

            return adjoin

        elif len(matrix) == 3:
            vertices = [item for sublist in matrix for item in sublist]
            adjoin = [[(vertices[4] * vertices[8]) - (vertices[5] * vertices[7]),
                       ((vertices[1] * vertices[8]) - (vertices[2] * vertices[7])) * -1,
                       (vertices[1] * vertices[5]) - (vertices[2] * vertices[4])],

                      [((vertices[3] * vertices[8]) - (vertices[5] * vertices[6])) * -1,
                       (vertices[0] * vertices[8]) - (vertices[2] * vertices[6]),
                       ((vertices[0] * vertices[5]) - (vertices[2] * vertices[3])) * -1],

                      [(vertices[3] * vertices[7]) - (vertices[4] * vertices[6]),
                       ((vertices[0] * vertices[7]) - (vertices[1] * vertices[6])) * -1,
                       (vertices[0] * vertices[4]) - (vertices[1] * vertices[3])]
                      ]
            return adjoin


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
            return matrix
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_matrix(matrix):
    for row in matrix:
        print(row)


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
            while True:
                try:
                    num_matrices = int(input("Enter the number of matrices to add: "))
                    matrices = prompt_matrices(num_matrices)
                    result = matrices[0]
                    for i in range(1, num_matrices):
                        result = add(result, matrices[i])
                    if result:
                        print("Result:")
                        print_matrix(result)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == 2:
            print("Subtraction")
            while True:
                try:
                    num_matrices = int(input("Enter the number of matrices to subtract: "))
                    matrices = prompt_matrices(num_matrices)
                    result = matrices[0]
                    for i in range(1, num_matrices):
                        result = subtract(result, matrices[i])
                    if result:
                        print("Result:")
                        print_matrix(result)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == 3:
            print("Multiplication")
            while True:
                try:
                    num_matrices = int(input("Enter the number of matrices to multiply: "))
                    matrices = prompt_matrices(num_matrices)
                    result = matrices[0]
                    for i in range(1, num_matrices):
                        result = multiply(result, matrices[i])
                    if result:
                        print("Result:")
                        print_matrix(result)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        elif choice == 4:
            print("Transpose")
            matrix = prompt_matrix()
            result = transpose(matrix)
            if result:
                print("Result:")
                print_matrix(result)

        elif choice == 5:
            print("Inverse")
            matrix = prompt_matrix()
            result = m_inverse(matrix)
            if result:
                print("Result:")
                print_matrix(result)

        elif choice == 6:
            print("Adjoint")
            matrix = prompt_matrix()
            result = adjoint(matrix)
            if result:
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

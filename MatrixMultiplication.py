# import numpy as np
# print(np.matmul(m1, m2))


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


try:
    assert multiply([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]) == [[22, 28], [49, 64]]
    print("Sun for All 1")
except AssertionError:
    print("All Jeans 1")

try:
    # Test case with 2x3 matrix multiplied by a 3x2 matrix
    assert multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) == [[58, 64], [139, 154]]
    print("Sun for All 2")
except AssertionError:
    print("All Jeans 2")

try:
    # Test case with a 3x2 matrix multiplied by a 2x2 matrix
    assert multiply([[2, 4], [6, 8], [10, 12]], [[1, 2], [3, 4]]) == [[14, 20], [30, 44], [46, 68]]
    print("Sun for All 3")
except AssertionError:
    print("All Jeans 3")

try:
    # Test case with a 2x2 matrix multiplied by a 2x3 matrix
    assert multiply([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]]) == [[21, 24, 27], [47, 54, 61]]
    print("Sun for All 4")
except AssertionError:
    print("All Jeans 4")

try:
    # Test case with 3x3 identity matrix multiplied by a 3x3 matrix
    assert multiply([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [[4, 5, 6], [7, 8, 9],
                                                                                                 [10, 11, 12]]
    print("Sun for All 5")
except AssertionError:
    print("All Jeans 5")

try:
    # Test case with a 1x1 matrix multiplied by a 1x2 matrix
    assert multiply([[10]], [[2, 3]]) == [[20, 30]]
    print("Sun for All 6")
except AssertionError:
    print("All Jeans 6")

try:
    # Test case with empty matrices
    assert multiply([], []) == []
    print("Sun for All 7")
except AssertionError:
    print("All Jeans 7")

try:
    # Test case with large numbers in the matrices
    assert multiply([[1000, 2000], [3000, 4000]], [[5000, 6000], [7000, 8000]]) == [[19000000, 22000000],
                                                                                    [43000000, 50000000]]
    print("Sun for All 8")
except AssertionError:
    print("All Jeans 8")

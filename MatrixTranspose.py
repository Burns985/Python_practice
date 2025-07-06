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


try:
    assert transpose([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    print("All Bright 1")
except AssertionError:
    print("All Jeans 1")

try:
    assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("All Bright 2")
except AssertionError:
    print("All Jeans 2")

try:
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    print("All Bright 3")
except AssertionError:
    print("All Jeans 3")

try:
    assert transpose([]) == []
    print("All Bright 4")
except AssertionError:
    print("All Jeans 4")

try:
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
    print("All Bright 5")
except AssertionError:
    print("All Jeans 5")

try:
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
    print("All Bright 6")
except AssertionError:
    print("All Jeans 6")

try:
    assert transpose([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]) == [[1, -4, 7], [-2, 5, -8], [3, -6, 9]]
    print("All Bright 7")
except AssertionError:
    print("All Jeans 7")

try:
    assert transpose([[1.5, 2.2], [3.7, 4.9]]) == [[1.5, 3.7], [2.2, 4.9]]
    print("All Bright 8")
except AssertionError:
    print("All Jeans 8")

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


try:
    assert add([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]) == [[2, 4, 6], [8, 10, 12]]
    print("Sun for All 1")
except AssertionError:
    print("All Jeans 1")

try:
    assert add([[1, 2], [3, 4]], [[-1, -2], [-3, -4]]) == [[0, 0], [0, 0]]
    print("Sun for All 2")
except AssertionError:
    print("All Jeans 2")

try:
    assert add([[1]], [[-1]]) == [[0]]
    print("Sun for All 3")
except AssertionError:
    print("All Jeans 3")

try:
    assert add([[1, 2], [3, 4]], [[-1, -2], [-3, -4], [5, 6]]) is None
    print("Sun for All 4")
except AssertionError:
    print("All Jeans 4")

try:
    assert add([[1, 2], [3, 4]], [[-1, -2], [-3, -4]]) == [[0, 0], [0, 0]]
    print("Sun for All 5")
except AssertionError:
    print("All Jeans 5")

try:
    assert add([[1, 2], [3, 4]], [[-1, -2], [-3, -4]]) == [[0, 0], [0, 0]]
    print("Sun for All 6")
except AssertionError:
    print("All Jeans 6")

try:
    assert add([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == [[10, 10, 10], [10, 10, 10],
                                                                                         [10, 10, 10]]
    print("Sun for All 7")
except AssertionError:
    print("All Jeans 7")

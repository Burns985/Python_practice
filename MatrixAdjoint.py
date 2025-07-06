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
                       (vertices[1] * vertices[5]) - (vertices[2] * vertices[4])]

                      , [((vertices[3] * vertices[8]) - (vertices[5] * vertices[6])) * -1,
                      (vertices[0] * vertices[8]) - (vertices[2] * vertices[6]),
                       ((vertices[0] * vertices[5]) - (vertices[2] * vertices[3])) * -1]

                      , [(vertices[3] * vertices[7]) - (vertices[4] * vertices[6]),
                      ((vertices[0] * vertices[7]) - (vertices[1] * vertices[6])) * -1,
                       (vertices[0] * vertices[4]) - (vertices[1] * vertices[3])]
                      ]
            return adjoin


try:
    assert adjoint([[1, 2], [3, 4]]) == [[4, -2], [-3, 1]]
    print("All Bright 1")
except AssertionError:
    print("All Jeans 1")

try:
    assert adjoint([[5, 1], [6, 2]]) == [[2, -1], [-6, 5]]
    print("All Bright 2")
except AssertionError:
    print("All Jeans 2")

try:
    assert adjoint([[4, 7, 2], [1, 3, 5], [8, 6, 9]]) == [[-3, -51, 29], [31, 20, -18], [-18, 32, 5]]
    print("All Bright 3")
except AssertionError:
    print("All Jeans 3")

try:
    assert adjoint([[1]]) == [[1]]
    print("All Bright 4")
except AssertionError:
    print("All Jeans 4")

try:
    assert adjoint([[2, 4], [6, 8]]) == [[8, -4], [-6, 2]]
    print("All Bright 5")
except AssertionError:
    print("All Jeans 5")
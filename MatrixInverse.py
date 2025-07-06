import numpy as np


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
                       (vertices[1] * vertices[5]) - (vertices[2] * vertices[4])]

                , [((vertices[3] * vertices[8]) - (vertices[5] * vertices[6])) * -1,
                   (vertices[0] * vertices[8]) - (vertices[2] * vertices[6]),
                   ((vertices[0] * vertices[5]) - (vertices[2] * vertices[3])) * -1]

                , [(vertices[3] * vertices[7]) - (vertices[4] * vertices[6]),
                   ((vertices[0] * vertices[7]) - (vertices[1] * vertices[6])) * -1,
                   (vertices[0] * vertices[4]) - (vertices[1] * vertices[3])]
                      ]
            inverse = [[round(x / det, 2) for x in row] for row in inverse]
            print(inverse)
            return inverse


try:
    assert m_inverse([[2, 1, 3], [1, 2, 4], [3, 4, 5]]) == [[6/11, -7/11, -2/11], [-7/11,  -1/11, 5/11], [2/11, 5/11, -3/11]]
    print("All Bright 1")
except AssertionError:
    print("All Jeans 1")

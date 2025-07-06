class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        m, n = len(matrix), len(matrix[0])
        vector = [[None] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                vector[i][j] = matrix[j][i]
        return vector

sol = Solution()
print([[1,2,3],[4,5,6],[7,8,9]])
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))
class Solution:
    def surfaceArea(self, grid) -> int:
        sur_area = 0
        count = 0
        for list in grid:
            for i in list:
                if not (i == 0):
                    sur_area += i*i
                    count += 1
        sur_area += count
        print(sur_area)
        return sur_area


assert Solution().surfaceArea([[1, 2], [3, 4]]) == 34

assert Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 32

assert Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 46

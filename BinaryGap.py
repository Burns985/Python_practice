class Solution:
    def binaryGap(self, n: int) -> int:
        binary_string = bin(n)[2:]

        max_gap = 0
        start = None

        for i, char in enumerate(binary_string):
            if char == "1":
                if start is not None:
                    gap = i - start
                    max_gap = max(max_gap, gap)
                start = i

        print(binary_string)
        return max_gap

sol = Solution()
print(sol.binaryGap(22))
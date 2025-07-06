import itertools


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if not nums:
            return 0
        sub_lists = []
        for i in reversed(range(2, len(nums))):
            sub_lists.append(itertools.combinations(nums, i))

        for sub in sub_lists:
            count = 0
            for s in sub:
                if list(s) == sorted(s):
                    count += 1
                print(list(s), sorted(s), count)
            if count != 0:
                break
        print(count)
        return count


try:
    assert Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2
except AssertionError:
    print("All Jeans 1")

try:
    assert Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3
except AssertionError:
    print("All Jeans 2")

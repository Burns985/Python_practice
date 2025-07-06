class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        n_sort = nums[:]
        n_sort.sort()
        print(n_sort, nums)
        if n_sort == nums or n_sort[::-1] == nums:
            return True
        return False


assert Solution().isMonotonic([1, 2, 2, 3]) == True

assert Solution().isMonotonic([6, 5, 4, 4]) == True

assert Solution().isMonotonic([1, 3, 2]) == False

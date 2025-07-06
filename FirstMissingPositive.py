class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        nums.append(0)
        nums = list(set(nums))
        nums.sort()

        count = 0
        for n in nums:
            if n > 0:
                count += 1
            if n == count:
                pass
            else:
                if n > 0:
                    print(count)
                    return count
        if nums[len(nums) - 1] + 1 > 0:
            return nums[len(nums) - 1] + 1
        else:
            return 1


try:
    print(Solution().firstMissingPositive([-10, -3, -100, -1000, -239, 1]))
    assert Solution().firstMissingPositive([-10, -3, -100, -1000, -239, 1]) == 2

    print("All Bright")
except AssertionError:
    print("All Jeans")

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in nums:
            if target - i in nums:
                if not nums.index(i) == nums.index(target - i):
                    return [nums.index(i), nums.index(target - i)]
                else:
                    if target - i in nums[nums.index(i) + 1:]:
                        return [nums.index(i), nums[nums.index(i) + 1:].index(target - i) + nums.index(i) + 1]


try:
    assert Solution().twoSum([2, 5, 5, 11], 10) == [1, 2]
except AssertionError:
    print("Incorrect 1")

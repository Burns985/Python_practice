class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        else:
            return nums[len(nums) // 2]


try:
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 5.0
except AssertionError:
    print("Incorrect 1")

try:
    assert Solution().findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7, 8]) == 4.5
except AssertionError:
    print("Incorrect 2")

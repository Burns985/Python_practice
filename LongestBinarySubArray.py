class Solution:
    def longestSubarray(self, nums: [int]) -> int:
        print("Method executed!")
        length = max_length = 0
        ignore_index = 0
        ignored = False
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                if not ignored:
                    ignored = True
                    ignore_index = i
                else:
                    ignored = False

            if nums[i] == 1 or ignored:
                if nums[i] == 1:
                    length += 1
            else:
                if max_length < length:
                    max_length = length
                ignored = False
                i = ignore_index
                length = 0
            i += 1

        if max_length < length:
            max_length = length

        if not (0 in nums):
            max_length = length - 1

        print(max_length)
        return max_length


try:
    assert Solution().longestSubarray([1, 1, 0, 1]) == 3
except AssertionError:
    print("Incorrect 1")

try:
    assert Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
except AssertionError:
    print("Incorrect 2")

try:
    assert Solution().longestSubarray([1, 1, 1, 1, 1, 1]) == 5
except AssertionError:
    print("Incorrect 3")

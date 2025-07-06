import itertools


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        return itertools.permutations(nums)

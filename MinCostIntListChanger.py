# My Code:

# class Solution:
#     def minCost(self, nums: [int], cost: [int]) -> int:
#         tent = sum(nums) // len(nums)
#         total_cost = 0
#         for i in range(len(nums)):
#             if nums[i] != tent:
#                 total_cost += abs(nums[i] - tent) * cost[i]
#         return total_cost


from itertools import accumulate


class Solution:
    def minCost(self, nums: [int], cost: [int]) -> int:
        ll = sorted([[nums[i], cost[i]] for i in range(len(cost))])
        c = list(accumulate([ll[i][1] for i in range(len(cost))]))
        nc = list(accumulate([ll[i][0] * ll[i][1] for i in range(len(cost))]))
        return min([ll[i][0]*(2*c[i]-c[len(cost)-1]) + (nc[len(cost)-1]-2*nc[i]) for i in range(len(cost))])


try:
    assert Solution().minCost(
        [735103, 366367, 132236, 133334, 808160, 113001, 49051, 735598, 686615, 665317, 999793, 426087, 587000, 649989,
         509946, 743518],
        [724182, 447415, 723725, 902336, 600863, 287644, 13836, 665183, 448859, 917248, 397790, 898215, 790754, 320604,
         468575, 825614]) == 1907611126748

    print("All Bright")
except AssertionError:
    print("All Jeans")

try:
    assert Solution().minCost([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]) == 0

    print("Sun for All")
except AssertionError:
    print("Love for All")

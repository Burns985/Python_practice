class Solution:
    def fairCandySwap(self, aliceSizes: [int], bobSizes: [int]) -> [int]:

        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                swap = []
                alice = aliceSizes
                bob = bobSizes
                temp = bob[j]
                bob[j] = alice[i]
                alice[i] = temp
                if sum(alice) == sum(bob):
                    swap.append(bob[j])
                    swap.append(alice[i])
                    return swap
                else:
                    alice[i] = bob[j]
                    bob[j] = temp




# class Solution:
#     def fairCandySwap(self, aliceSizes: [int], bobSizes: [int]) -> [int]:
#         sum_alice = sum(aliceSizes)
#         sum_bob = sum(bobSizes)
#
#         diff = (sum_alice - sum_bob) // 2
#         alice_set = set(aliceSizes)
#
#         for bob in bobSizes:
#             alice = bob + diff
#             print(diff, alice, bob)
#             if alice in alice_set:
#                 return [alice, bob]
#
#         return []  # Return an empty list if no fair swap is found
#
# assert Solution().fairCandySwap([1, 1], [2, 2]) == [1, 2]

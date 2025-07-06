import itertools


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(list(itertools.permutations(''.join([str(num) for num in list(range(1, (n + 1)))]), n))[k - 1])

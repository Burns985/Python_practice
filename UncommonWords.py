class Solution:
    def uncommonFromSentences(self, s1, s2) -> []:
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        uncommon = []
        length = max(len(l1), len(l2))
        for i in range(length):
            if i < len(l1) and l1[i] not in l2 and l1[i] not in uncommon:
                uncommon.append(l1[i])
            if i < len(l2) and l2[i] not in l1 and l2[i] not in uncommon:
                uncommon.append(l2[i])
            if i < len(l1) and l1[i] in uncommon and (l1[i] in l1[i + 1:] or l1[i] in l1[:i] or l1[i] in l2):
                uncommon.remove(l1[i])
            if i < len(l2) and l2[i] in uncommon and (l2[i] in l2[i + 1:] or l2[i] in l2[:i] or l2[i] in l1):
                uncommon.remove(l2[i])
        return uncommon


solution = Solution()

st1 = "apple apple"
st2 = "banana"

assert solution.uncommonFromSentences(st1, st2) == ["banana"]

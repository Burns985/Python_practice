class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        strs.sort()
        anagrams = []
        for i in strs:
            j = list(i)
            j.sort()
            anagrams.append("".join(j))
        set_anagrams = set(anagrams)
        anagrams_list = []
        for i in set_anagrams:
            count = 0
            add_list = []
            while i in anagrams[count:] and count < len(anagrams):
                index = anagrams.index(i, count)
                add_list.append(strs[index])
                count = index + 1
            anagrams_list.append(add_list)
        return anagrams_list

# from collections import defaultdict
#
# class Solution:
#     def groupAnagrams(self, strs: [str]):
#         anagrams_map = defaultdict(list)
#
#         for word in strs:
#             sorted_word = "".join(sorted(word))
#             anagrams_map[sorted_word].append(word)
#
#         return list(anagrams_map.values())


try:
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"],
                                                                                    ["ate", "eat", "tea"]]

    print("All Bright")
except AssertionError:
    print("All Jeans")


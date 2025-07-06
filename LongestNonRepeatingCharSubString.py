class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = max_length = 0
        sub = ""
        for char in s:
            if char in sub:
                if max_length < length:
                    max_length = length
                sub = sub[sub.index(char) + 1:] + char
                length = len(sub)
            else:
                sub = sub + char
                length += 1

        if max_length < length:
            max_length = length
        return max_length


# Best Code

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_length = 0
#         start = 0
#         char_map = {}
#
#         for end in range(len(s)):
#             if s[end] in char_map:
#                 start = max(start, char_map[s[end]] + 1)
#             char_map[s[end]] = end
#             max_length = max(max_length, end - start + 1)
#
#         return max_length


try:
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
    print("All Bright")
except AssertionError:
    print("All Jeans")

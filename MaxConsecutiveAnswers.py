class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_length = 0
        left = right = 0
        counts = {'T': 0, 'F': 0}

        while right < len(answerKey):
            counts[answerKey[right]] += 1
            while min(counts.values()) > k:
                counts[answerKey[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

# My Version
# class Solution:
#     def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
#         f_count = 0
#         t_count = 0
#         for i in answerKey:
#             if "F" == i:
#                 f_count += 1
#             else:
#                 t_count += 1
#         if t_count == f_count:
#             if len(answerKey) == k:
#                 return k
#             else:
#                 if k > f_count:
#                     return t_count + f_count
#                 else:
#                     return t_count + k or f_count + k
#
#         else:
#             count = 0
#             answer_key = answerKey
#             if t_count > f_count:
#                 if f_count == 0:
#                     return t_count
#                 for key in answerKey:
#                     if count < k:
#                         if key == "F":
#                             s = list(answer_key)
#                             s[answer_key.index(key)] = "T"
#                             answer_key = "".join(s)
#                             count += 1
#                 max_length = 0
#                 t_count = 0
#                 if "F" in answer_key:
#                     for i in answer_key:
#                         if "F" == i:
#                             if t_count > max_length:
#                                 max_length = t_count
#                             t_count = 0
#                         else:
#                             t_count += 1
#                     if max_length < f_count:
#                         max_length = f_count
#                     return max_length
#                 else:
#                     return len(answer_key)
#
#             else:
#                 if t_count == 0:
#                     return f_count
#                 for key in answerKey:
#                     if count <= k:
#                         if key == "T":
#                             s = list(answer_key)
#                             s[answer_key.index(key)] = "F"
#                             answer_key = "".join(s)
#                             count += 1
#                 max_length = 0
#                 f_count = 0
#                 if "T" in answer_key:
#                     for i in answer_key:
#                         if "T" == i:
#                             if f_count > max_length:
#                                 max_length = f_count
#                             f_count = 0
#                         else:
#                             f_count += 1
#                     if max_length < f_count:
#                         max_length = f_count
#                     return max_length
#                 else:
#                     return len(answer_key)
#
#
# try: assert Solution().maxConsecutiveAnswers(
# "T",
# 32) == 85 except AssertionError: print("Incorrect")

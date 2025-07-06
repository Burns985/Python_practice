# def longestValidParentheses(self, s: str) -> int:
#     if ")" in s[s.index("("):] and "(" in s[::-1][s[::-1].index(")")::]:
#         return len(s) - s.index("(") - s[::-1].index(")") - 1
#     else:
#         return 0


# def longestValidParentheses(self, s: str) -> int:
#     a = s[s.index("("):] if "(" in s else -1
#     b = s[::-1][s[::-1].index(")")::] if ")" in s else -1
#
#     if a == -1 or b == -1:
#         return 0
#     else:
#         s_list = list(s)
#         print(s_list)
#         count = 0
#         i = 0
#         while "(" in s_list and ")" in s_list:
#             if "(" in s_list and ")" in s_list:
#                 if s_list.index("(") < s_list.index(")"):
#                     if s_list[i] == "(":
#                         s_list.remove("(")
#                         s_list.remove(")")
#                         count += 2
#                         print(s_list)
#                         i = 0
#                 else:
#                     if "(" in s_list[s_list.index("(") + 1 :]:
#                         s_list.remove("(")
#                         s_list.remove(")")
#                         count += 2
#                         print(s_list)
#                         i = 0
#                     else:
#                         break
#         return count

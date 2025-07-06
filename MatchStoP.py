class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) > len(p):
            return False
        if not len(s) == len(p):
            return True
        else:
            offset = 0
            if "*" in p or "." in p:
                for i in range(len(p)):
                    if p[i] == "*":
                        if s[i] == p[i-1] or "." == p[i-1]:
                            lit = list(p)
                            lit[i] = s[i]
                            p = "".join(lit)
                    if p[i] == ".":
                        lit = list(p)
                        print(lit)
                        lit[i] = s[i]
                        p = "".join(lit)
        print(p)
        return s in p


# try:
#     assert Solution().isMatch("aab", "c*a*b")
# except AssertionError:
#     print("Incorrect 1")

# try:
#     assert Solution().isMatch("aa", "a*")
# except AssertionError:
#     print("Incorrect 2")

try:
    assert Solution().isMatch("ab", ".*")
except AssertionError:
    print("Incorrect 3")

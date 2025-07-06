class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "*" in p:
            return True
        else:
            if len(s) != len(p):
                return False
            elif "?" in p:
                for i in range(len(s)):
                    if s[i] is not p[i]:
                        if p[i] != "?":
                            return False
                        else:
                            j = list(p)
                            j[j.index("?")] = s[i]
                            p = "".join(j)
        if s == p:
            return True
        return False

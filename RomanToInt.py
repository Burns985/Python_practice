class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman = 0
        while s != "":
            if "M" == s[0]:
                roman += 1000
                s = s.replace("M", "", 1)
            elif "CM" == s[0:2]:
                roman += 900
                s = s.replace("CM", "", 1)
            elif "D" == s[0]:
                roman += 500
                s = s.replace("D", "", 1)
            elif "CD" == s[0:2]:
                roman += 400
                s = s.replace("CD", "", 1)
            elif "C" == s[0]:
                roman += 100
                s = s.replace("C", "", 1)
            elif "XC" == s[0:2]:
                roman += 90
                s = s.replace("XC", "", 1)
            elif "L" == s[0]:
                roman += 50
                s = s.replace("L", "", 1)
            elif "XL" == s[0:2]:
                roman += 40
                s = s.replace("XL", "", 1)
            elif "X" == s[0]:
                roman += 10
                s = s.replace("X", "", 1)
            elif "IX" == s[0:2]:
                roman += 9
                s = s.replace("IX", "", 1)
            elif "V" == s[0]:
                roman += 5
                s = s.replace("V", "", 1)
            elif "IV" == s[0:2]:
                roman += 4
                s = s.replace("IV", "", 1)
            elif "I" == s[0]:
                roman += 1
                s = s.replace("I", "", 1)
        return roman


try:
    assert Solution().romanToInt("MCMXCIV") == 1994
    print("All Bright")
except AssertionError:
    print("All Jeans")

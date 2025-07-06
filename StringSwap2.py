class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if s == goal:
            # Check if there are repeating characters in the string
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        if not (len(s) == len(goal)):
            return False

        for char in s:
            if not (char in goal):
                return False

        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)

        if len(diff_indices) != 2:
            return False
        else:
            i, j = diff_indices
            if s[i] == goal[j] and s[j] == goal[i]:
                return True

        return False
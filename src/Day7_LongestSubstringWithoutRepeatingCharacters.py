class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return size

        current_longest = 0
        sub = ""

        for c in s:
            if c not in sub:
                sub += c
                if len(sub) > current_longest:
                    current_longest = len(sub)
            else:
                sub = f"{sub.split(c)[1]}{c}"

        return current_longest
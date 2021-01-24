class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        char_counts = {}
        for c in s:
            if c in char_counts:
                char_counts[c] = char_counts[c] + 1
            else:
                char_counts[c] = 1
        values = char_counts.values()
        num_odd = 0

        for n in values:
            if n == 1 or n % 2 != 0:
                num_odd += 1

        return num_odd < 2

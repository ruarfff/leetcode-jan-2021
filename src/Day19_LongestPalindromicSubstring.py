class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # If we have a string with all single letters this will actually be the answer
        ans = s[0]

        for i in range(n):
            # We need to scan i and i+1 to account for palindromes with multiple letters from the middle e.g. bb or abba
            dist = max(self.scan(s, n, i, i), self.scan(s, n, i, i + 1))
            # If we discovered a palindrome longer than the current answer
            if dist > len(ans):
                # set our answer to a substring using dist to calculate the appropriate indices
                ans = s[i - (dist - 1) // 2 : (i + dist // 2) + 1]

        return ans

    def scan(self, s: str, n: int, l: int, r: int) -> int:
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1
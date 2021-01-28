class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l = 0
        ans = 0
        for i in range(1, n + 1):            
            if i & (i - 1) == 0:
                l += 1
            ans = ((ans << l) | i) % (10 ** 9 + 7)
        return ans
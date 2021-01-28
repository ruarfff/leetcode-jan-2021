from collections import deque


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        d = deque()
        i = n - 1
        while i >= 0:
            a = min(k - i, 26)
            d.extendleft(chr(a + ord("a") - 1))
            k -= a
            i -= 1

        return "".join(d)

from typing import List
import math


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_ops = 0
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1

        for n in counts:
            diff = k - n
            if diff in counts and counts[diff] > 0:
                ops = 0
                if n == k // 2:
                    ops = math.floor(counts[n] // 2)
                else:
                    ops = min(counts[n], counts[diff])

                max_ops += ops
                counts[diff] = counts[diff] - ops
                counts[n] = counts[n] - ops

        return max_ops
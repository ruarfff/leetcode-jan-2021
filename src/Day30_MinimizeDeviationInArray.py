from typing import List
import heapq
import math


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        vals = []
        minimum = math.inf
        minimum_deviation = math.inf

        for n in nums:
            if n % 2 == 0:
                vals.append(-n)
                minimum = min(minimum, n)   
            else:
                evened = n * 2
                vals.append(-evened)
                minimum = min(minimum, evened)

        heapq.heapify(vals)

        while vals:
            e = -heapq.heappop(vals)
            minimum_deviation = min(minimum_deviation, e - minimum)

            if e % 2 != 0:
                return minimum_deviation
            e = e // 2
            minimum = min(minimum, e)
            heapq.heappush(vals, -e)

        return minimum_deviation
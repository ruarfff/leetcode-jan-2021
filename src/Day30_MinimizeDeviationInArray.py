from typing import List
import heapq
import math


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        minimum = math.inf
        minimum_deviation = math.inf

        for n in nums:
            if n % 2 == 0:
                evens.append(-n)
                minimum = min(minimum, n)
            else:
                evens.append(-n * 2)
                minimum = min(minimum, n * 2)

        heapq.heapify(evens)

        while evens:
            e = -heapq.heappop(evens)
            minimum_deviation = min(minimum_deviation, e - minimum)

            if e % 2 != 0:
                return minimum_deviation

            minimum = min(minimum, e // 2)
            heapq.heappush(evens, -e // 2)

        return minimum_deviation
from typing import List
import collections


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        count = collections.Counter()
        ans = 0
        for row in grid:
            for i, val in enumerate(row):
                if val:
                    for x in range(i + 1, len(row)):
                        if row[x]:
                            ans += count[i, x]
                            count[i, x] += 1
        return ans
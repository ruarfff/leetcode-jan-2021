from typing import List
import math
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        diff = [[math.inf] * col for _ in range(row)]
        diff[0][0] = 0
        visited = [[False] * col for _ in range(row)]
        queue = [(0, 0, 0)]
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if (
                    0 <= adjacent_x < row
                    and 0 <= adjacent_y < col
                    and not visited[adjacent_x][adjacent_y]
                ):
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y] - heights[x][y]
                    )
                    max_difference = max(current_difference, diff[x][y])
                    if diff[adjacent_x][adjacent_y] > max_difference:
                        diff[adjacent_x][adjacent_y] = max_difference
                        heapq.heappush(queue, (max_difference, adjacent_x, adjacent_y))
        return diff[-1][-1]

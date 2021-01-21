from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        rem = k - n

        for i in range(n):
            while len(stack) > max(0, rem + i) and nums[i] < stack[-1]:
                stack.pop()
            stack.append(nums[i])

        return stack[:k]

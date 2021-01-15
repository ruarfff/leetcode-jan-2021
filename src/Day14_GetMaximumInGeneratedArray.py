class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1

        for i in range(1, n):
            x = 2 * i
            if x > 1 and x <= n:
                nums[x] = nums[i]
            if x + 1 > 1 and x + 1 <= n:
                nums[x + 1] = nums[i] + nums[i + 1]

        return max(nums)
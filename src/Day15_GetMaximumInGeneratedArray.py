class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l = n + 1
        if n == 0:
            return 0
        nums = [0] * l
        nums[1] = 1
        current_max = 1

        for i in range(1, l):
            x = 2 * i
            if x > 1 and x <= n:
                nums[x] = nums[i]
            if x + 1 > 1 and x + 1 <= n:
                nums[x + 1] = nums[i] + nums[i + 1]
            current_max = max(current_max, nums[i])

        return current_max
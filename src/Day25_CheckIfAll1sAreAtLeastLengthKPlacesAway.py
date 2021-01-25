from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        current_dist = k
        for n in nums:
            if n == 1:
                if current_dist < k:
                    return False
                current_dist = 0
            else:
                current_dist += 1

        return True
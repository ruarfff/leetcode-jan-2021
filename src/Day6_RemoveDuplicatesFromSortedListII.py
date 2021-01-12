from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_numbers = 0
        next_expected = 1

        for x in arr:
            while x != next_expected:
                missing_numbers += 1
                if missing_numbers == k:
                    return next_expected
                next_expected += 1
            next_expected += 1

        if len(arr) > 0 and missing_numbers < k:
            return arr[-1] + (k - missing_numbers)

        return k
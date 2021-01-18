import pytest
from .Day18_MaxNumberOfKSumPairs import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4], 5, 2),
        ([3, 1, 3, 4, 3], 6, 1),
        ([3, 5, 1, 5], 2, 0),
        ([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2, 2),
    ],
)
def test_max_operations(nums, k, expected):
    assert s.maxOperations(nums, k) == expected
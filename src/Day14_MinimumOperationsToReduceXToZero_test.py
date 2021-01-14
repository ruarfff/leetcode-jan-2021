import pytest
from .Day14_MinimumOperationsToReduceXToZero import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,x,expected",
    [([1, 1, 4, 2, 3], 5, 2), ([5, 6, 7, 8, 9], 4, -1), ([3, 2, 20, 1, 1, 3], 10, 5)],
)
def test_min_operations(nums, x, expected):
    assert s.minOperations(nums, x) == expected

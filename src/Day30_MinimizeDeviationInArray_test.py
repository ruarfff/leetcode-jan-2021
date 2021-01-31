import pytest
from .Day30_MinimizeDeviationInArray import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], 1),
        ([4, 1, 5, 20, 3], 3),
        ([2, 10, 8], 3),
    ],
)
def test_minimum_deviation(nums, expected):
    assert s.minimumDeviation(nums) == expected

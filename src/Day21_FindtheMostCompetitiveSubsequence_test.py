import pytest
from .Day21_FindtheMostCompetitiveSubsequence import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3, 5, 2, 6], 2, [2, 6]),
        ([2, 4, 3, 3, 5, 4, 9, 6], 4, [2, 3, 3, 4]),
    ],
)
def test_most_competitive(nums, k, expected):
    assert s.mostCompetitive(nums, k) == expected
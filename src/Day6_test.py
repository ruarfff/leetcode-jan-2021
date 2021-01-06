import pytest
from .Day6 import Solution

s = Solution()


@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([2, 3, 4, 7, 11], 5, 9),
        ([1, 2, 3, 4], 2, 6),
        ([9, 10, 11, 12], 4, 4),
        ([], 2, 2),
        ([], 0, 0),
    ],
)
def test_find_kth_positive(arr, k, expected):
    assert s.findKthPositive(arr, k) == expected

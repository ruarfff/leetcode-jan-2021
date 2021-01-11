import pytest
from .Day11 import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums1,m,nums2,n,expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_length_of_longest_substring(nums1, m, nums2, n, expected):
    s.merge(nums1, m, nums2, n)
    assert nums1 == expected

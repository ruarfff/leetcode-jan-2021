import pytest
from .Day31_NextPermutation import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
    ],
)
def test_next_permutation(nums, expected):
    s.nextPermutation(nums)

    assert nums == expected

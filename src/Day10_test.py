import pytest
from .Day10 import Solution

s = Solution()


@pytest.mark.parametrize(
    "instructions,expected",
    [
        ([1, 5, 6, 2], 1),
        ([1, 2, 3, 6, 5, 4], 3),
        ([1, 3, 3, 3, 2, 4, 2, 1, 2], 4),
    ],
)
def test_length_of_longest_substring(instructions, expected):
    assert s.createSortedArray(instructions) == expected

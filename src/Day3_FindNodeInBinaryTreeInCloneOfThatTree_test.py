import pytest
from .Day3_FindNodeInBinaryTreeInCloneOfThatTree import Solution

s = Solution()


@pytest.mark.parametrize("input,expected", [(2, 2), (1, 1), (3, 3), (4, 8)])
def test_gives_number_of_beautiful_arrangements(input, expected):
    assert s.countArrangement(input) == expected

import pytest
from .Day28_SmallestStringWithAGivenNumericValue import Solution

s = Solution()


@pytest.mark.parametrize(
    "n,k,expected",
    [
        (3, 27, "aay"),
        (5, 73, "aaszz"),
    ],
)
def test_get_smallest_string(n, k, expected):
    assert s.getSmallestString(n, k) == expected
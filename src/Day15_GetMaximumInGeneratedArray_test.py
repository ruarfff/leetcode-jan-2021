import pytest
from .Day15_GetMaximumInGeneratedArray import Solution

s = Solution()


@pytest.mark.parametrize(
    "n,expected",
    [
        (7, 3),
        (2, 1),
        (3, 2),
        (0, 0),
    ],
)
def test_get_maximum_generated(n, expected):
    assert s.getMaximumGenerated(n) == expected

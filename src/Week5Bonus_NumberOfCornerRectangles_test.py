import pytest
from .Week5Bonus_NumberOfCornerRectangles import Solution

s = Solution()


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]], 1),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),
        ([[1, 1, 1, 1]], 0),        
    ],
)
def test_count_corner_rectangles(grid, expected):
    assert s.countCornerRectangles(grid) == expected

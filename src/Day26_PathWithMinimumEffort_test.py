import pytest
from .Day26_PathWithMinimumEffort import Solution

s = Solution()


@pytest.mark.parametrize(
    "heights,expected",
    [
        ([[1,2,2],[3,8,2],[5,3,5]], 2),
        ([[1,2,3],[3,8,4],[5,3,5]], 1),
        ([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0),        
    ],
)
def test_minimum_effort_path(heights, expected):
    assert s.minimumEffortPath(heights) == expected
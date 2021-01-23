import pytest
from .Day23_SortMatrixDiagonally import Solution

s = Solution()


@pytest.mark.parametrize(
    "mat,expected",
    [
        (
            [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]],
            [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]],
        ),
    ],
)
def test_diagonal_sort(mat, expected):
    assert s.diagonalSort(mat) == expected
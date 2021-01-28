import pytest
from .Day27_ConcatenationOfConsecutiveBinaryNumbers import Solution

s = Solution()


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (3, 27),
        (12, 505379714),
    ],
)
def test_concatenated_binary(n, expected):
    assert s.concatenatedBinary(n) == expected
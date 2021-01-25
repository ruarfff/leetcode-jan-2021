import pytest
from .Day25_CheckIfAll1sAreAtLeastLengthKPlacesAway import Solution

s = Solution()


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1,0,0,0,1,0,0,1], 2, True),
        ([1,0,0,1,0,1], 2, False),
        ([1,1,1,1,1], 0, True),
        ([0,1,0,1], 1, True)
    ],
)
def test_k_length_apart(nums, k, expected):
    assert s.kLengthApart(nums, k) == expected
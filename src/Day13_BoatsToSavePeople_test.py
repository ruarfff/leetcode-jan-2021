import pytest
from .Day13_BoatsToSavePeople import Solution

s = Solution()


@pytest.mark.parametrize(
    "people,limit,expected",
    [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
        ([2, 2], 6, 1),
        ([3, 1, 7], 7, 2),
        ([2, 4], 5, 2),
    ],
)
def test_num_rescue_boats(people, limit, expected):
    assert s.numRescueBoats(people, limit) == expected

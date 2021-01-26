import pytest
from .Week4Bonus_OneEditDistance import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("ab", "acb", True),
        ("", "", False),
        ("a", "", True),
        ("", "A", True),
        ("c", "c", False),
        ("ab", "acd", False),
    ],
)
def test_is_one_edit_distance(s, t, expected):
    assert Solution().isOneEditDistance(s, t) == expected
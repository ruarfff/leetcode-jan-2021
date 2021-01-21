import pytest
from .Day20_ValidParentheses import Solution

sol = Solution()


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("[", False),
        ("((", False),
    ],
)
def test_is_valid_parentheses(s, expected):
    assert sol.isValid(s) == expected
import pytest
from .Day19_LongestPalindromicSubstring import Solution

s = Solution()


@pytest.mark.parametrize(
    "string,expected",
    [("babad", "bab"), ("cbbd", "bb"), ("a", "a"), ("ac", "a"), ("bb", "bb")],
)
def test_longest_palindrome(string, expected):
    assert s.longestPalindrome(string) == expected
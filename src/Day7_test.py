import pytest
from .Day7 import Solution

s = Solution()


@pytest.mark.parametrize(
    "input,expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("ababc", 3),
        ("dvdf", 3),
        ("", 0),
    ],
)
def test_length_of_longest_substring(input, expected):
    assert s.lengthOfLongestSubstring(input) == expected
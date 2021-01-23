import pytest
from .Day22_DetermineIfTwoStringsAreClose import Solution

s = Solution()


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        ("abc", "bca", True),
        ("a", "aa", False),
        ("cabbba", "abbccc", True),
        ("cabbba", "aabbss", False),
    ],
)
def test_close_strings(word1, word2, expected):
    assert s.closeStrings(word1, word2) == expected
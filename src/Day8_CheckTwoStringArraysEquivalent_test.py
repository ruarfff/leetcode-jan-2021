import pytest
from .Day8_CheckTwoStringArraysEquivalent import Solution

s = Solution()


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True),
    ],
)
def test_array_strings_are_equal(word1, word2, expected):
    assert s.arrayStringsAreEqual(word1, word2) == expected
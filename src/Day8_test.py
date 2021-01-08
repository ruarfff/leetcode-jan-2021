import pytest
from .Day8 import Solution

s = Solution()


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True),        
    ],
)
def test_length_of_longest_substring(word1, word2, expected):
    assert s.arrayStringsAreEqual(word1, word2) == expected
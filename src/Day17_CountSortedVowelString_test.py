import pytest
from .Day17_CountSortedVowelString import Solution

s = Solution()


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 5),
        (2, 15),
        (33, 66045),
    ],
)
def test_countVowelStrings(n, expected):
    assert s.count_vowel_strings(n) == expected

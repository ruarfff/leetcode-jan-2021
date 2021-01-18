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
def test_count_vowel_strings(n, expected):
    assert s.countVowelStrings(n) == expected

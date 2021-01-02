import pytest
from .Week1Bonus import Solution

p = Solution()


@pytest.mark.parametrize("test_input", ["code", "abc"])
def test_cannot_permute(test_input):
    assert not p.canPermutePalindrome(test_input)


@pytest.mark.parametrize("test_input", ["aab", "carerac", "a", "aa"])
def test_can_permute(test_input):
    assert p.canPermutePalindrome(test_input)
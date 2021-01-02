import pytest
from .Week1Bonus import Solution

s = Solution()


@pytest.mark.parametrize("test_input", ["code", "abc"])
def test_cannot_permute(test_input):
    assert not s.canPermutePalindrome(test_input)


@pytest.mark.parametrize("test_input", ["aab", "carerac", "a", "aa"])
def test_can_permute(test_input):
    assert s.canPermutePalindrome(test_input)
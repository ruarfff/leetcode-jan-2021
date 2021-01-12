import pytest
from typing import List
from .util import ListNode, toListNode, toList
from .Day5_MergeTwoSortedLists import Solution

s = Solution()


@pytest.mark.parametrize(
    "input,expected",
    [
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 2, 3, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([2, 3, 4], [2, 3, 4]),
        ([1, 1], []),
        ([0], [0]),
        ([], []),
        ([1, 1, 2, 2], []),
    ],
)
def test_remove_duplicates(input, expected):
    assert toList(s.deleteDuplicates(toListNode(input))) == expected

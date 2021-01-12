import pytest
from typing import List
from .util import ListNode, toListNode, toList
from .Day12_AddTwoNumbers import Solution

s = Solution()


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    list_root1 = toListNode(l1)
    list_root2 = toListNode(l2)
    assert toList(s.addTwoNumbers(list_root1, list_root2)) == expected
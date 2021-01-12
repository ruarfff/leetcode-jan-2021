import pytest
from typing import List
from .util import ListNode, toListNode, toList
from .Day4_BeautifulArrangement import Solution

s = Solution()


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([1, 9, 22], [-3, 4, 30], [-3, 1, 4, 9, 22, 30]),
        (
            [-3, 4, 31, 49],
            [-20, -20, -3, 1, 4, 9, 22, 40, 40],
            [-20, -20, -3, -3, 1, 4, 4, 9, 22, 31, 40, 40, 49],
        ),
        ([], [0], [0]),
        ([], [], []),
    ],
)
def test_merge_sorted_list(l1, l2, expected):
    list_root1 = toListNode(l1)
    list_root2 = toListNode(l2)
    assert toList(s.mergeTwoLists(list_root1, list_root2)) == expected

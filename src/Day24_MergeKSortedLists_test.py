import pytest
from .util import toListNode, toList
from .Day24_MergeKSortedLists import Solution

s = Solution()


@pytest.mark.parametrize(
    "lists,expected",
    [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]), ([], []), ([[]], [])],
)
def test_merge_k_lists(lists, expected):
    assert toList(s.mergeKLists(list(map(lambda x: toListNode(x), lists)))) == expected

@pytest.mark.parametrize(
    "lists,expected",
    [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]), ([], []), ([[]], [])],
)
def test_merge_k_lists2(lists, expected):
    assert toList(s.mergeKLists2(list(map(lambda x: toListNode(x), lists)))) == expected
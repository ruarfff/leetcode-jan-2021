import pytest
from typing import List
from .Week3Bonus_NestedListWeightSum import Solution
from .util import NestedInteger

s = Solution()


@pytest.mark.parametrize(
    "num_list,expected",
    [
        ([[1, 1], 2, [1, 1]], 10),
        ([1, [4, [6]]], 27),
        ([0], 0),
    ],
)
def test_depth_sum(num_list, expected):
    x = build_nested_list(num_list)
    for n in x:
        print(n)
        print(n.isInteger())
    assert s.depthSum(x) == expected


def build_nested_list(num_list) -> List[NestedInteger]:
    nestedList = []
    for n in num_list:
        if isinstance(n, int):
            nestedList.append(NestedInteger(n))
        else:
            nestedList.append(list_to_nested_int(n))
    return nestedList


def list_to_nested_int(nums):
    ni = NestedInteger()
    for n in nums:
        if isinstance(n, int):
            ni.add(NestedInteger(n))
        else:
            ni.add(list_to_nested_int(n))
    return ni

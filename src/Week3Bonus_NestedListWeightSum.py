from typing import List
from .util import NestedInteger


class Solution:
    def depthSumWithDepth(self, nestedList: List[NestedInteger], depth: int):
        sum = 0
        for n in nestedList:
            if n.isInteger():
                sum += n.getInteger() * depth
            else:
                sum += self.depthSumWithDepth(n.getList(), depth + 1)
        return sum

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.depthSumWithDepth(nestedList, 1)
from typing import List
from .util import NestedInteger


class Solution:
    def depthSumWithDepth(self, nestedList: List[NestedInteger], depth: int):
        sum = 0
        # Iterate over the list. If we hit an int, add it to the sum multiplying by depth
        for n in nestedList:
            if n.isInteger():
                sum += n.getInteger() * depth
            else:
                # Recursively sump up all the sub lists incrementing the depth as needed
                sum += self.depthSumWithDepth(n.getList(), depth + 1)
        return sum

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # Start at depth 1
        return self.depthSumWithDepth(nestedList, 1)
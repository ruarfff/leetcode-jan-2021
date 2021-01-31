from collections import deque, OrderedDict
from typing import List
from .util import TreeNode


class TravesalItem:
    def __init__(self, node, row, col):
        self.node = node
        self.row = row
        self.col = col


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        grid_items = []
        traversal = {}

        traversal_queue = deque([TravesalItem(root, 0, 0)])
        while traversal_queue:
            ti = traversal_queue.popleft()
            if ti.node is not None:
                grid_items.append((ti.col, ti.row, ti.node.val))
                traversal_queue.append(
                    TravesalItem(ti.node.left, ti.row + 1, ti.col - 1)
                )
                traversal_queue.append(
                    TravesalItem(ti.node.right, ti.row + 1, ti.col + 1)
                )

        for col, row, val in sorted(grid_items):
            if col not in traversal:
                traversal[col] = []
            traversal[col].append(val)

        return traversal.values()
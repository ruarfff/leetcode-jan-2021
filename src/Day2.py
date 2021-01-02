from .util import TreeNode


def search(tree: TreeNode, val: int) -> TreeNode:
    if tree.val == val:
        return tree

    if tree.left is not None:
        l = search(tree.left, val)
        if l is not None:
            return l
    if tree.right is not None:
        r = search(tree.right, val)
        if r is not None:
            return r
    return None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        return search(cloned, target.val)

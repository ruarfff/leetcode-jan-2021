import copy
from .util import TreeNode
from .Day2_FindNodeInBinaryTreeInCloneOfThatTree import Solution

s = Solution()


def test_find_node():
    tree = TreeNode(7)
    tree.left = TreeNode(4)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(19)

    original = tree
    clone = copy.deepcopy(tree)

    assert s.getTargetCopy(original, clone, tree.right).val == 3

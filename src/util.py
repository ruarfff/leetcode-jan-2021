class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def compareTrees(a: TreeNode, b: TreeNode) -> bool:
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return (
            (a.val == b.val)
            and compareTrees(a.left, b.left)
            and compareTrees(a.right, b.right)
        )
    return False


def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return None

    if root.val < val:
        if root.right is None:
            root.right = TreeNode(val)
        else:
            insertIntoBST(root.right, val)

    else:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            insertIntoBST(root.left, val)

    return root


def serialize(root: TreeNode) -> str:
    if root is None or root.val is None:
        return ""

    return f"{root.val},{serialize(root.left)}{serialize(root.right)}"


def deserialize(data: str) -> TreeNode:
    if len(data) == 0:
        return None

    head, *tail = list(
        map(
            (lambda x: int(x)),
            filter((lambda x: x is not None and x != ""), data.split(",")),
        )
    )

    root = TreeNode(head)
    for i in tail:
        insertIntoBST(root, i)

    return root

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def toListNode(original_list: List[int]):
    if len(original_list) == 0:
        return None
    head, *tail = original_list
    root_node = ListNode(head)
    next_node = root_node

    for x in tail:
        new_node = ListNode(x)
        next_node.next = new_node
        next_node = new_node

    return root_node


def toList(list_node: ListNode):
    new_list = []

    if list_node is None:
        return new_list

    node = list_node
    new_list.append(node.val)

    next_node = node

    while next_node.next is not None:
        next_node = next_node.next
        new_list.append(next_node.val)

    return new_list

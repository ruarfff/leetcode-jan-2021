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

    def __gt__(self, ln2):
        return self.val > ln2.val

    def __lt__(self, ln2):
        return self.val < ln2.val


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


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is None:
            self.ni = []
        else:
            self.ni = value

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.ni, int)

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.ni.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.ni = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.ni
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger():
            return None

        return self.ni

    def __str__(self):
        if self.isInteger():
            return f"{self.ni}"
        else:
            string = ""
            for n in self.ni:
                string = f"{n}, {string}"
            return string

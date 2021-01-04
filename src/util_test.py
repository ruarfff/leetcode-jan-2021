from .util import (
    TreeNode,
    ListNode,
    serialize,
    deserialize,
    compareTrees,
    toList,
    toListNode,
)


def test_empty_serialize():
    assert deserialize(serialize(None)) is None


def test_can_serialize_and_deserialize():
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)

    serialized = serialize(tree)
    assert serialized == "2,1,3,"

    deserialized = deserialize(serialized)
    assert compareTrees(deserialized, tree)


def test_to_list_empty():
    l = None

    assert toList(l) == []


def test_to_list_one():
    l = ListNode()

    assert toList(l) == [0]


def test_to_list():
    l = ListNode(2)
    l.next = ListNode(3)
    l.next.next = ListNode(4)

    assert toList(l) == [2, 3, 4]


def test_to_list_node_empty():
    assert toListNode([]) == None


def test_to_list_node_empty():
    assert toListNode([1]).val == ListNode(1).val


def test_to_list_node_empty():
    ln = toListNode([1, 2, 3])
    assert ln.val == 1
    assert ln.next.val == 2
    assert ln.next.next.val == 3

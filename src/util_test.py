from .util import serialize, deserialize, TreeNode, compareTrees


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

class Solution:
    def findRoot(self, tree: List["Node"]) -> "Node":
        c = {}
        n = {}
        for node in tree:
            n[node.val] = node
            if node.children is not None:
                for ch in node.children:
                    c[ch.val] = True
        for k in n:
            if k not in c:
                return n[k]
        return None
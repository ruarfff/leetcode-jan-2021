from typing import List


class BinaryIndexTree:
    def __init__(self, space: int):
        self.space = space
        # Init tree to all zeros with 'space' nodes
        self.tree = [0] * space

    def getCost(self, index):
        result = 0
        while index >= 1:
            result += self.tree[index]
            index -= index & -index
        return result

    def update(self, index, value):
        while index < self.space:
            self.tree[index] += value
            index += index & -index


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
        # Init tree ensuring we have a node for each number
        tree = BinaryIndexTree(max(instructions) + 2)
        cost = 0
        for i in range(n):
            leftCost = tree.getCost(instructions[i])
            rightCost = i - tree.getCost(instructions[i] + 1)
            cost += min(leftCost, rightCost)
            tree.update(instructions[i] + 1, 1)
        mod = 1000000007
        return cost % mod
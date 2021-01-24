from typing import List
from .util import ListNode
from queue import PriorityQueue


class Solution:
    def build_queue(self, lists: List[ListNode]) -> PriorityQueue:
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l), False)
        return q

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        current = head
        q = self.build_queue(lists)

        while not q.empty():
            val, list_node = q.get()
            current.next = ListNode(val)
            current = current.next
            next_node = list_node.next
            if next_node:
                q.put((next_node.val, next_node), False)

        return head.next
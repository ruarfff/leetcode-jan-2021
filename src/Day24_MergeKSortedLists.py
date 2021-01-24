from typing import List
from .util import ListNode
from queue import PriorityQueue


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    current = head
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l1
            l1 = current.next.next
        current = current.next
    current.next = l2 if l2 else l1
    return head.next


class Solution:
    def build_queue(self, lists: List[ListNode]) -> PriorityQueue:
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l), False)
        return q

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None

        step = 1
        while step < k:
            for i in range(0, k - step, step * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + step])
            step *= 2

        return lists[0]
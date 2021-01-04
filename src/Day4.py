from .util import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        out = None
        l_next = None

        if l1.val > l2.val:
            out = l2
            l_next = l1
        else:
            out = l1
            l_next = l2

        out_next = out

        while l_next is not None:
            if out_next.next is None:
                out_next.next = l_next
                l_next = None
            elif l_next.val >= out_next.val and l_next.val <= out_next.next.val:
                new_node = ListNode(l_next.val, out_next.next)
                out_next.next = new_node
                l_next = l_next.next

            out_next = out_next.next

        return out
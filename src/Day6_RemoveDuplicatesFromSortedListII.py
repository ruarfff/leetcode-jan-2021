from .util import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        holder = ListNode(0, head)
        dummy_head = holder
        next_node = head

        while next_node:
            if next_node.next is not None and next_node.next.val == next_node.val:
                while (
                    next_node.next is not None and next_node.val == next_node.next.val
                ):
                    next_node = next_node.next
                dummy_head.next = next_node.next
            else:
                dummy_head = dummy_head.next
            next_node = next_node.next

        return holder.next

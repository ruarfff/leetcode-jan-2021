from .util import ListNode


def add(carry: int, l1: ListNode, l2: ListNode, out: ListNode):
    x = l1.val if l1 is not None else 0
    y = l2.val if l2 is not None else 0
    ans = x + y + carry
    if ans >= 10:
        carry = 1
        ans = ans - 10
    else:
        carry = 0
    out.val = ans
    l1_next = l1.next if l1 is not None else None
    l2_next = l2.next if l2 is not None else None

    if l1_next or l2_next or carry > 0:
        out.next = ListNode()
        add(carry, l1_next, l2_next, out.next)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        carry = 0

        add(carry, l1, l2, head)
        return head
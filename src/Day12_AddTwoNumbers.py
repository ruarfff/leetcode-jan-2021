from .util import ListNode


def add(carry: int, l1: ListNode, l2: ListNode):
    x = l1.val
    y = l2.val if l2 is not None else 0
    ans = x + y + carry
    if ans >= 10:
        carry = 1
        ans = ans - 10
    else:
        carry = 0
    l1.val = ans
    l2_next = l2.next if l2 is not None else None

    if l2_next or carry > 0:
        if l1.next is None:
            l1.next = ListNode()

        add(carry, l1.next, l2_next)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        add(carry, l1, l2)
        return l1
# %%
from selectors import EpollSelector
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        # Recursive solution, more elegant, heavy on the stack for large lists
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        val = sum % 10
        carry = int(sum > 9)

        if not (carry or l1 or l2):
            return ListNode(val)
        else:
            return ListNode(val, self.addTwoNumbers(l1, l2, carry))

        # # Iterative solution, decently fast, easy on the call stack
        # curr_node = ListNode()
        # start = curr_node
        # carry_over = 0

        # while True:
        #     if (l1 and l2):
        #         sum = l1.val + l2.val + carry_over
        #         add_val, carry_over = sum % 10, int(sum > 9)
        #         l1 = l1.next
        #         l2 = l2.next
        #     elif l1:
        #         sum = l1.val + carry_over
        #         add_val, carry_over = sum % 10, int(sum > 9)
        #         l1 = l1.next
        #     elif l2:
        #         sum = l2.val + carry_over
        #         add_val, carry_over = sum % 10, int(sum > 9)
        #         l2 = l2.next
        #     else:
        #         add_val = carry_over
        #         carry_over = 0

        #     curr_node.val = add_val

        #     if not (l1 or l2 or carry_over):
        #         return start

        #     tmp = ListNode()
        #     curr_node.next = tmp
        #     curr_node = tmp
        # %%

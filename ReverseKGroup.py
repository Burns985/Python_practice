from typing import Optional


class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> ListNode:
        if not head or k == 1:
            return head

        # Helper function to reverse a group of nodes
        def reverse_group(prev, next, count):
            last = prev.next
            curr = last.next
            while curr is not next:
                last.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = last.next
            return last

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        count = 0

        while head:
            count += 1
            if count % k == 0:
                prev = reverse_group(prev, head.next, k)
                head = prev.next
            else:
                head = head.next

        return dummy.next
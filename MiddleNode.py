class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head : ListNode) -> ListNode:
            middle_node = head
            while head and head.next:
                middle_node = middle_node.next
                head = head.next.next

            return middle_node
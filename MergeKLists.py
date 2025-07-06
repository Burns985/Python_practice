# MergeSinglyLinkedListAscendingOrder


class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution:
    def mergeKLists(self, lists: [[ListNode]]):
        if not lists:
            return None

        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        if not values:
            return None

        values.sort()
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

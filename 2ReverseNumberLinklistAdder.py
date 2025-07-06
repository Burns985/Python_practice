class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> [ListNode]:
        num1 = num2 = ""
        temp = l1
        while temp is not None:
            num1 = num1 + (str(temp.val))
            temp = temp.next

        inter = l2
        while inter is not None:
            num2 = num2 + (str(inter.val))
            inter = inter.next

        n = "".join(list(num1)[::-1])
        m = "".join(list(num2)[::-1])

        total = str(int(m) + int(n))[::-1]
        head = ListNode(int(total[0]))
        self.addNodes(head, total[1:])
        return head

    count = 0

    def addNodes(self, root, s):
        if not len(s) == self.count:
            root.next = ListNode(int(s[self.count]))
            self.count += 1
            self.addNodes(root.next, s)


try:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    print(result.val, result.next.val, result.next.next.val)
    assert result.val == 7
    print("All night")
    assert result.next.val == 0
    print("All Bright")
    assert result.next.next.val == 8
    print("Sun for All")
except AssertionError:
    print("All Jeans")


# Optimized ChatGPT code
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(0)  # Dummy node to keep track of the head
#         curr = dummy  # Pointer to the current node
#         carry = 0  # Carry value for addition
#
#         while l1 or l2 or carry:
#             # Calculate the sum of the current digits and the carry
#             sum_val = carry
#             if l1:
#                 sum_val += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum_val += l2.val
#                 l2 = l2.next
#
#             # Create a new node with the sum value
#             curr.next = ListNode(sum_val % 10)
#             carry = sum_val // 10
#
#             # Move the current pointer to the next node
#             curr = curr.next
#
#         return dummy.next  # Return the head of the resulting linked list

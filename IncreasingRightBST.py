class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    nodes = []

    def increasingBST(self, root) -> TreeNode:
        self.listBST(root, None)
        print(self.nodes)

    def listBST(self, root, prev):
        if root is not None:
            # if root.left is not None or root.right is not None:
            self.listBST(root.left, root)
            self.nodes.append(root.val)
            self.listBST(root.right, root)
        else:
            if prev is not None and (prev.left is not None or prev.right is not None):
                self.nodes.append(None)


print("[5, 3, 6, 2, 4, None, 8, 1, None, None, None ,7, 9]")
head = TreeNode(5)
head.left = TreeNode(3)
head.right = TreeNode(6)
head.left.left = TreeNode(2)
head.left.right = TreeNode(4)
head.right.right = TreeNode(8)
head.left.left.left = TreeNode(1)
head.right.right.left = TreeNode(7)
head.right.right.right = TreeNode(9)

Solution().increasingBST(head)











# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     nodes = []
#     links = {}
#     count = 0
#
#     def increasingBST(self, root) -> TreeNode:
#         self.sizeBST(root)
#         self.listBST(root, None, 1)
#         print(self.nodes)
#
#         for s in str(self.links).split(","):
#             print(s)
#
#         print(self.count)
#         return None
#
#     def listBST(self, root, prev, i):
#         if root is not None:
#             Solution.links[root.val] = i
#             self.listBST(root.left, root, i+1)
#             self.listBST(root.right, root, i+1)
#         else:
#             if prev is not None:
#                 if self.check_key(Solution.links, "None " + str(prev.val)):
#                     Solution.links["NoneR " + str(prev.val)] = i
#
#                     Solution.links["None " + str(prev.val)] = i
#
#     def check_key(self, dictionary, value):
#         return value in dictionary
#
#     def sizeBST(self, root):
#         if root is not None:
#             self.count += 1
#             self.nodes.append(root.val)
#             self.sizeBST(root.left)
#             self.sizeBST(root.right)
#
#
# print("[5, 3, 6, 2, 4, None, 8, 1, None, None, None ,7, 9]")
# head = TreeNode(5)
# head.left = TreeNode(3)
# head.right = TreeNode(6)
# head.left.left = TreeNode(2)
# head.left.right = TreeNode(4)
# head.right.right = TreeNode(8)
# head.left.left.left = TreeNode(1)
# head.right.right.left = TreeNode(7)
# head.right.right.right = TreeNode(9)
#
# Solution().increasingBST(head)

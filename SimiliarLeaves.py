from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    leaves = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.preorder(root1)
        leaves1 = Solution.leaves
        Solution.leaves = []
        self.preorder(root2)
        leaves2 = Solution.leaves
        Solution.leaves = []
        if leaves1 == leaves2:
            return True
        else:
            return False

    def preorder(self, root: Optional[TreeNode]):
        if root is not None:
            if root.left is None and root.right is None:
                Solution.leaves.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

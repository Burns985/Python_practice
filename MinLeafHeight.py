class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    count = 0
    min_height = 0
    print(min_height)

    def minDepth(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.min_height

    def traverse(self, root):
        if self.count > self.min_height != 0:
            return
        if root is not None:
            self.count += 1
            self.traverse(root.left)
            self.traverse(root.right)
            if root.left is None and root.right is None:
                if self.count < self.min_height or self.min_height == 0:
                    self.min_height = self.count
            self.count -= 1

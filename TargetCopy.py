class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target) if original.left else None
        right = self.getTargetCopy(original.right, cloned.right, target) if original.right else None
        return left or right
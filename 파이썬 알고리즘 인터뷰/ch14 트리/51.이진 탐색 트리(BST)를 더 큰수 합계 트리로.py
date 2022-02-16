from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        self.bstToGst(root.left)
        return root





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
# root.left.right = TreeNode
# root.right.left = TreeNode(4)
root.right.right = TreeNode(4)
# root.right.left.left = TreeNode(6)
# root.right.left.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)
print(Solution().isBalanced(root))
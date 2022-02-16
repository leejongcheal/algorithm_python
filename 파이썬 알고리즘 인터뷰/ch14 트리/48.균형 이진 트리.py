# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        return check(root) != -1



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

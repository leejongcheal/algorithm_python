from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(now):
            if now is None:
                return -1
            left = dfs(now.left)
            right = dfs(now.right)
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(Solution().diameterOfBinaryTree(root))

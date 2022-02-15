from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        q = deque()
        max_hight = 0
        if root is None:
            return 0
        q.append((root, 1))
        while q:
            now, hight = q.popleft()
            max_hight = max(max_hight, hight)
            if now.left is not None:
                q.append((now.left, hight + 1))
            if now.right is not None:
                q.append((now.right, hight + 1))
        return max_hight

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        q = deque([root])
        while q:
            depth += 1
            for _ in range(len(q)):
                now = q.popleft()
                if now.left:
                    q.append(now.left)
                if now.right:
                    q.append(now.right)
        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth2(root))
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        q = deque([root])
        while q:
            now = q.popleft()
            if now:
                now.left, now.right = now.right, now.left
                q.append(now.left)
                q.append(now.right)
        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(Solution().invertTree(root))
print(root.val)
print(root.left.val, root.right.val)
print(root.left.left.val, root.left.right.val,root.right.left.val, root.right.right.val)
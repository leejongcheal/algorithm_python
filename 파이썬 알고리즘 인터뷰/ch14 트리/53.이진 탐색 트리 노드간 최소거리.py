class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = int(1e10)
    prev = -int(1e10)

    def minDiffInBST(self, root: [TreeNode]) -> int:
        if not root:
            return None
        self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        self.minDiffInBST(root.right)
        return self.result

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
print(Solution().minDiffInBST(root))
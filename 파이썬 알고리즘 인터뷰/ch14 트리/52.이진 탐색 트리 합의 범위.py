from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        now = root.val
        if now < low:
            return self.rangeSumBST(root.right, low, high)
        elif now > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return now + \
                   self.rangeSumBST(root.left, low, high) + \
                   self.rangeSumBST(root.right, low, high)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

# root.right.left = TreeNode(6)
root.right.right = TreeNode(18)

# root.right.left.left = TreeNode(6)
# root.right.left.right = TreeNode(7)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(4)
print(Solution().rangeSumBST(root, 7, 15))

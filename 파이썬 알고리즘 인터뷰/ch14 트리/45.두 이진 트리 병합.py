class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: [TreeNode], root2: [TreeNode]) -> [TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 or root2




root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
# root.left.right = TreeNode
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
# root1.left.left = TreeNode()
root1.left.right = TreeNode(4)
# root1.right.left = TreeNode(7)
root1.right.right = TreeNode(7)
ans = Solution().mergeTrees(root, root1)

print(1)
